
import pygame
import sys

from settings import (
    ANCHO,
    ALTO,
    FPS,
    TITULO,
    VIDAS_INICIALES
)

from player import Jugador
from levels.level1 import Nivel1
from levels.level2 import Nivel2
from levels.level3 import Nivel3
from graphics import dibujar_fondo
from ui.interface import Interfaz


pygame.init()

pantalla = pygame.display.set_mode(
    (ANCHO, ALTO)
)

pygame.display.set_caption(TITULO)

reloj = pygame.time.Clock()

interfaz = Interfaz()

estado = "menu"
numero_nivel = 1

nivel = Nivel1()
jugador = Jugador(*nivel.inicio)

vidas = VIDAS_INICIALES
puntuacion_total = 0

# Tiempo efectivo de juego, sin contar pausas
tiempo_jugado = 0.0

# Protección temporal después de perder una vida
proteccion_restante = 0.0
DURACION_PROTECCION = 1.5



def crear_nivel(numero):

    niveles = {
        1: Nivel1,
        2: Nivel2,
        3: Nivel3
    }

    clase = niveles.get(numero)

    if clase is None:
        return None

    return clase()


def reiniciar_partida():
    global proteccion_restante
    global numero_nivel, nivel, jugador
    global vidas, puntuacion_total
    global tiempo_jugado

    numero_nivel = 1
    nivel = crear_nivel(numero_nivel)
    jugador = Jugador(*nivel.inicio)

    vidas = VIDAS_INICIALES
    puntuacion_total = 0
    tiempo_jugado = 0.0


def cambiar_nivel():

    global numero_nivel, nivel, jugador
    global puntuacion_total, estado

    puntuacion_total += nivel.puntos
    numero_nivel += 1

    nuevo = crear_nivel(numero_nivel)

    if nuevo is None:
        estado = "victoria"
        return

    nivel = nuevo
    jugador = Jugador(*nivel.inicio)



def perder_vida():

    global vidas, jugador, estado
    global proteccion_restante

    if proteccion_restante > 0:
        return

    vidas -= 1

    if vidas <= 0:
        estado = "game_over"
    else:
        jugador = Jugador(*nivel.inicio)
        proteccion_restante = DURACION_PROTECCION



def ejecutar_boton(nombre):

    global estado

    if nombre == "iniciar":
        reiniciar_partida()
        estado = "jugando"

    elif nombre == "continuar":
        estado = "jugando"

    elif nombre == "reiniciar":
        reiniciar_partida()
        estado = "jugando"

    elif nombre == "menu":
        estado = "menu"

    elif nombre == "salir":
        return False

    return True


def main():

    global estado, tiempo_jugado, proteccion_restante
    ejecutando = True

    while ejecutando:

        delta = min(
            reloj.tick(FPS) / 1000.0,
            0.05
        )

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                ejecutando = False

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    estado = "menu"

                elif evento.key == pygame.K_p:

                    if estado == "jugando":
                        estado = "pausa"

                    elif estado == "pausa":
                        estado = "jugando"

                elif evento.key == pygame.K_r:

                    if estado in (
                        "game_over",
                        "victoria"
                    ):
                        reiniciar_partida()
                        estado = "jugando"

            elif evento.type == pygame.MOUSEBUTTONDOWN:

                if evento.button == 1:

                    if estado != "jugando":

                        nombre = interfaz.obtener_boton(
                            evento.pos
                        )

                        if nombre is not None:
                            ejecutando = ejecutar_boton(
                                nombre
                            )

        if not ejecutando:
            break

        # Actualizacion del juego
        if estado == "jugando":

            tiempo_jugado += delta
            
            if proteccion_restante > 0:
                proteccion_restante = max(
                    0.0,
                    proteccion_restante - delta
                )


            jugador.actualizar(
                nivel.plataformas
            )

            resultado = nivel.actualizar(
                jugador
            )

            if resultado == "trampa":
                perder_vida()

            elif resultado == "completado":
                cambiar_nivel()

            if (
                estado == "jugando"
                and jugador.rect.top > ALTO
            ):
                perder_vida()

        # Dibujar pantallas
        if estado == "menu":

            interfaz.menu(pantalla)

        elif estado == "jugando":

            dibujar_fondo(
                pantalla,
                numero_nivel,
                pygame.time.get_ticks()
            )

            nivel.dibujar(pantalla)
            jugador.dibujar(pantalla)

            puntos = (
                puntuacion_total + nivel.puntos
            )

            interfaz.hud(
                pantalla,
                numero_nivel,
                vidas,
                puntos,
                int(tiempo_jugado)
            )

        elif estado == "pausa":

            interfaz.pausa(pantalla)

        elif estado == "game_over":

            puntos = (
                puntuacion_total + nivel.puntos
            )

            interfaz.game_over(
                pantalla,
                puntos
            )

        elif estado == "victoria":

            interfaz.victoria(
                pantalla,
                puntuacion_total,
                int(tiempo_jugado)
            )

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
