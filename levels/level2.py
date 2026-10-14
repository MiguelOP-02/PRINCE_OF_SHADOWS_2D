
import pygame

from settings import (
    ANCHO,
    ALTO,
    DORADO,
    GRIS,
    ROJO,
    VERDE
)


class Nivel2:

    def __init__(self):

        # Plataformas del segundo nivel
        self.plataformas = [
            pygame.Rect(0, 550, 180, 50),
            pygame.Rect(250, 550, 170, 50),
            pygame.Rect(490, 550, 170, 50),
            pygame.Rect(750, 550, 250, 50),

            pygame.Rect(170, 450, 150, 20),
            pygame.Rect(390, 365, 150, 20),
            pygame.Rect(610, 280, 150, 20),
            pygame.Rect(820, 195, 160, 20)
        ]

        # Monedas
        self.monedas = [
            pygame.Rect(80, 510, 20, 20),
            pygame.Rect(225, 410, 20, 20),
            pygame.Rect(450, 325, 20, 20),
            pygame.Rect(670, 240, 20, 20),
            pygame.Rect(900, 155, 20, 20)
        ]

        # Pinchos en plataformas
        self.trampas = [
            pygame.Rect(330, 530, 60, 20),
            pygame.Rect(560, 530, 60, 20),
            pygame.Rect(790, 530, 60, 20)
        ]

        # Puerta de salida
        self.puerta = pygame.Rect(
            925, 130, 40, 65
        )

        # Posicion inicial del jugador
        self.inicio = (45, 450)

        # Puntuacion obtenida en este nivel
        self.puntos = 0

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

        # Plataformas
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

        # Monedas
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

        # Pinchos
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
                    (
                        min(
                            x + ancho_pincho,
                            trampa.right
                        ),
                        trampa.bottom
                    )
                ]

                pygame.draw.polygon(
                    pantalla,
                    ROJO,
                    puntos
                )

        # Puerta
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
