
import pygame

from settings import (
    ANCHO,
    ALTO,
    BLANCO,
    DORADO,
    ROJO,
    AZUL_OSCURO
)


class Interfaz:

    def __init__(self):

        self.titulo = pygame.font.SysFont(
            "arial", 52, bold=True
        )

        self.subtitulo = pygame.font.SysFont(
            "arial", 26, bold=True
        )

        self.normal = pygame.font.SysFont(
            "arial", 22
        )

        self.pequena = pygame.font.SysFont(
            "arial", 18
        )

        self.botones = {}

    def texto(self, pantalla, mensaje, fuente,
              color, centro):

        imagen = fuente.render(
            str(mensaje), True, color
        )

        pantalla.blit(
            imagen,
            imagen.get_rect(center=centro)
        )

    def boton(self, pantalla, nombre, mensaje,
              x, y, ancho=280, alto=55):

        rect = pygame.Rect(x, y, ancho, alto)
        mouse = pygame.mouse.get_pos()
        encima = rect.collidepoint(mouse)

        color = (
            (255, 215, 120)
            if encima else DORADO
        )

        pygame.draw.rect(
            pantalla,
            color,
            rect,
            border_radius=12
        )

        self.texto(
            pantalla,
            mensaje,
            self.normal,
            (20, 25, 40),
            rect.center
        )

        self.botones[nombre] = rect

    def obtener_boton(self, posicion):

        for nombre, rect in self.botones.items():

            if rect.collidepoint(posicion):
                return nombre

        return None

    def fondo(self, pantalla):

        pantalla.fill(AZUL_OSCURO)

        pygame.draw.rect(
            pantalla,
            DORADO,
            (0, 0, ANCHO, 7)
        )

    def menu(self, pantalla):

        self.botones.clear()
        self.fondo(pantalla)

        self.texto(
            pantalla,
            "PRINCE OF SHADOWS",
            self.titulo,
            DORADO,
            (ANCHO // 2, 155)
        )

        self.texto(
            pantalla,
            "La aventura del templo perdido",
            self.normal,
            BLANCO,
            (ANCHO // 2, 225)
        )

        self.boton(
            pantalla,
            "iniciar",
            "INICIAR JUEGO",
            ANCHO // 2 - 140,
            300
        )

        self.boton(
            pantalla,
            "salir",
            "SALIR",
            ANCHO // 2 - 140,
            375
        )

        self.texto(
            pantalla,
            "Proyecto colaborativo - Python + Pygame",
            self.pequena,
            (155, 165, 185),
            (ANCHO // 2, 540)
        )

    def hud(self, pantalla, nivel, vidas,
            puntos, segundos):

        # Panel superior
        panel = pygame.Surface(
            (ANCHO, 90),
            pygame.SRCALPHA
        )

        panel.fill((10, 15, 30, 215))
        pantalla.blit(panel, (0, 0))

        minutos = segundos // 60
        resto = segundos % 60

        tiempo = f"{minutos:02}:{resto:02}"

        self.texto(
            pantalla,
            f"VIDAS: {vidas}",
            self.normal,
            ROJO,
            (105, 27)
        )

        self.texto(
            pantalla,
            f"NIVEL {nivel}",
            self.subtitulo,
            BLANCO,
            (ANCHO // 2, 27)
        )

        self.texto(
            pantalla,
            f"PUNTOS: {puntos}",
            self.normal,
            DORADO,
            (ANCHO - 130, 27)
        )

        self.texto(
            pantalla,
            f"TIEMPO: {tiempo}",
            self.pequena,
            BLANCO,
            (ANCHO // 2, 66)
        )

        self.texto(
            pantalla,
            "P: Pausa | ESC: Menu",
            self.pequena,
            BLANCO,
            (140, 66)
        )

    def pausa(self, pantalla):

        self.botones.clear()
        self.fondo(pantalla)

        self.texto(
            pantalla,
            "JUEGO EN PAUSA",
            self.titulo,
            DORADO,
            (ANCHO // 2, 180)
        )

        self.boton(
            pantalla,
            "continuar",
            "CONTINUAR",
            ANCHO // 2 - 140,
            280
        )

        self.boton(
            pantalla,
            "menu",
            "MENU PRINCIPAL",
            ANCHO // 2 - 140,
            360
        )

    def game_over(self, pantalla, puntos):

        self.botones.clear()
        self.fondo(pantalla)

        self.texto(
            pantalla,
            "GAME OVER",
            self.titulo,
            ROJO,
            (ANCHO // 2, 170)
        )

        self.texto(
            pantalla,
            f"Puntuacion: {puntos}",
            self.normal,
            BLANCO,
            (ANCHO // 2, 250)
        )

        self.boton(
            pantalla,
            "reiniciar",
            "REINTENTAR",
            ANCHO // 2 - 140,
            310
        )

        self.boton(
            pantalla,
            "menu",
            "MENU PRINCIPAL",
            ANCHO // 2 - 140,
            390
        )

    def victoria(self, pantalla, puntos, segundos):

        self.botones.clear()
        self.fondo(pantalla)

        self.texto(
            pantalla,
            "¡VICTORIA!",
            self.titulo,
            DORADO,
            (ANCHO // 2, 135)
        )

        self.texto(
            pantalla,
            "Has completado los 3 niveles",
            self.normal,
            BLANCO,
            (ANCHO // 2, 215)
        )

        self.texto(
            pantalla,
            f"Puntuacion final: {puntos}",
            self.subtitulo,
            DORADO,
            (ANCHO // 2, 270)
        )

        self.texto(
            pantalla,
            f"Tiempo: {segundos // 60:02}:{segundos % 60:02}",
            self.normal,
            BLANCO,
            (ANCHO // 2, 315)
        )

        self.boton(
            pantalla,
            "reiniciar",
            "JUGAR OTRA VEZ",
            ANCHO // 2 - 140,
            370
        )

        self.boton(
            pantalla,
            "menu",
            "MENU PRINCIPAL",
            ANCHO // 2 - 140,
            445
        )
