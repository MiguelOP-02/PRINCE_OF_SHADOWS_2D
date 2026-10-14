
import pygame

from settings import (
    ANCHO,
    ALTO,
    DORADO,
    GRIS,
    ROJO,
    VERDE
)


class Nivel1:

    def __init__(self):

        # Plataformas del nivel
        self.plataformas = [
            pygame.Rect(0, 550, 1000, 50),
            pygame.Rect(150, 440, 170, 20),
            pygame.Rect(380, 350, 170, 20),
            pygame.Rect(610, 260, 170, 20),
            pygame.Rect(830, 170, 150, 20)
        ]

        # Monedas
        self.monedas = [
            pygame.Rect(90, 510, 20, 20),
            pygame.Rect(220, 400, 20, 20),
            pygame.Rect(450, 310, 20, 20),
            pygame.Rect(680, 220, 20, 20),
            pygame.Rect(900, 130, 20, 20)
        ]

        # Trampas de pinchos
        self.trampas = [
            pygame.Rect(340, 530, 90, 20),
            pygame.Rect(570, 530, 90, 20)
        ]

        # Puerta de salida
        self.puerta = pygame.Rect(
            930, 105, 40, 65
        )

        # Posicion inicial
        self.inicio = (50, 450)

        # Puntuacion del nivel
        self.puntos = 0

        # Estado de finalizacion
        self.completado = False

    def actualizar(self, jugador):

        # Recoger monedas
        for moneda in self.monedas[:]:

            if jugador.rect.colliderect(moneda):

                self.monedas.remove(moneda)
                self.puntos += 100

        # Detectar trampas
        for trampa in self.trampas:

            if jugador.rect.colliderect(trampa):
                return "trampa"

        # Detectar puerta
        if jugador.rect.colliderect(self.puerta):

            self.completado = True
            return "completado"

        return None

    def dibujar(self, pantalla):

        # Dibujar plataformas
        for plataforma in self.plataformas:

            pygame.draw.rect(
                pantalla,
                GRIS,
                plataforma,
                border_radius=4
            )

            pygame.draw.rect(
                pantalla,
                DORADO,
                (
                    plataforma.x,
                    plataforma.y,
                    plataforma.width,
                    5
                ),
                border_radius=2
            )

        # Dibujar monedas
        for moneda in self.monedas:

            pygame.draw.ellipse(
                pantalla,
                DORADO,
                moneda
            )

            pygame.draw.ellipse(
                pantalla,
                (255, 235, 150),
                moneda,
                2
            )

        # Dibujar trampas
        for trampa in self.trampas:

            ancho_pincho = 20

            for x in range(
                trampa.left,
                trampa.right,
                ancho_pincho
            ):

                puntos = [
                    (x, trampa.bottom),
                    (x + ancho_pincho // 2, trampa.top),
                    (min(x + ancho_pincho, trampa.right),
                     trampa.bottom)
                ]

                pygame.draw.polygon(
                    pantalla,
                    ROJO,
                    puntos
                )

        # Dibujar puerta
        pygame.draw.rect(
            pantalla,
            DORADO,
            self.puerta,
            border_radius=5
        )

        interior = self.puerta.inflate(
            -12, -10
        )

        pygame.draw.rect(
            pantalla,
            (100, 65, 30),
            interior,
            border_radius=3
        )

        pygame.draw.circle(
            pantalla,
            VERDE,
            (
                self.puerta.right - 12,
                self.puerta.centery
            ),
            4
        )
        
        # Panel de instrucciones del Nivel 1
        panel = pygame.Surface(
            (370, 175),
            pygame.SRCALPHA
        )

        panel.fill((15, 20, 35, 210))
        pantalla.blit(panel, (15, 65))

        fuente_titulo = pygame.font.SysFont(
            "arial", 22, bold=True
        )

        fuente_texto = pygame.font.SysFont(
            "arial", 17
        )

        titulo = fuente_titulo.render(
            "NIVEL 1 - TUTORIAL",
            True,
            DORADO
        )

        pantalla.blit(titulo, (30, 78))

        instrucciones = [
            "A / D o FLECHAS: Moverse",
            "ESPACIO / W / ARRIBA: Saltar",
            "SHIFT: Correr",
            "Recoge monedas y evita los pinchos",
            "Llega a la puerta dorada"
        ]

        for indice, mensaje in enumerate(instrucciones):
            texto = fuente_texto.render(
                mensaje,
                True,
                (255, 255, 255)
            )

            pantalla.blit(
                texto,
                (30, 112 + indice * 24)
            )

        

