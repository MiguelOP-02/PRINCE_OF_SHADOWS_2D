
import pygame

from settings import (
    DORADO,
    GRIS,
    ROJO,
    VERDE
)


class Nivel3:

    def __init__(self):

        # Plataformas del templo final
        self.plataformas = [
            pygame.Rect(0, 550, 155, 50),
            pygame.Rect(220, 550, 130, 50),
            pygame.Rect(415, 550, 130, 50),
            pygame.Rect(620, 550, 130, 50),
            pygame.Rect(825, 550, 175, 50),

            pygame.Rect(125, 455, 140, 20),
            pygame.Rect(315, 365, 140, 20),
            pygame.Rect(510, 275, 140, 20),
            pygame.Rect(705, 185, 140, 20),
            pygame.Rect(850, 115, 130, 20)
        ]

        # Monedas del nivel final
        self.monedas = [
            pygame.Rect(75, 510, 20, 20),
            pygame.Rect(190, 415, 20, 20),
            pygame.Rect(380, 325, 20, 20),
            pygame.Rect(575, 235, 20, 20),
            pygame.Rect(770, 145, 20, 20),
            pygame.Rect(915, 75, 20, 20)
        ]

        # Trampas
        self.trampas = [
            pygame.Rect(270, 530, 60, 20),
            pygame.Rect(465, 530, 60, 20),
            pygame.Rect(665, 530, 60, 20),
            pygame.Rect(870, 530, 60, 20)
        ]

        # Puerta final
        self.puerta = pygame.Rect(
            930, 50, 40, 65
        )

        # Posicion inicial
        self.inicio = (40, 450)

        # Puntuacion
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

        # Detectar puerta final
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

        # Dibujar pinchos
        for trampa in self.trampas:

            ancho_pincho = 20

            for x in range(
                trampa.left,
                trampa.right,
                ancho_pincho
            ):

                puntos = [
                    (x, trampa.bottom),
                    (
                        x + ancho_pincho // 2,
                        trampa.top
                    ),
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

        # Dibujar puerta final
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
