
import pygame
import math
from settings import ANCHO, ALTO


def dibujar_fondo(pantalla, numero_nivel, tiempo):

    colores = {
        1: ((24, 30, 55), (70, 55, 75)),
        2: ((40, 22, 45), (100, 45, 50)),
        3: ((18, 22, 40), (65, 40, 75))
    }

    superior, inferior = colores.get(
        numero_nivel, colores[1]
    )

    # Fondo degradado
    for y in range(ALTO):

        factor = y / ALTO

        color = tuple(
            int(
                superior[i] * (1 - factor)
                + inferior[i] * factor
            )
            for i in range(3)
        )

        pygame.draw.line(
            pantalla,
            color,
            (0, y),
            (ANCHO, y)
        )

    # Columnas antiguas
    for x in range(40, ANCHO, 170):

        pygame.draw.rect(
            pantalla,
            (65, 58, 77),
            (x, 90, 45, ALTO - 90)
        )

        pygame.draw.rect(
            pantalla,
            (105, 85, 105),
            (x - 10, 80, 65, 18)
        )

        pygame.draw.rect(
            pantalla,
            (105, 85, 105),
            (x - 10, ALTO - 45, 65, 18)
        )

        pygame.draw.line(
            pantalla,
            (85, 73, 95),
            (x + 15, 100),
            (x + 15, ALTO - 50),
            4
        )

    # Techo del templo
    pygame.draw.rect(
        pantalla,
        (55, 45, 65),
        (0, 65, ANCHO, 22)
    )

    # Antorchas
    for x in (130, 500, 870):

        pygame.draw.rect(
            pantalla,
            (120, 80, 50),
            (x - 5, 170, 10, 35)
        )

        oscilacion = math.sin(
            tiempo * 0.008 + x
        ) * 5

        puntos = [
            (x, 135 + oscilacion),
            (x - 15, 170),
            (x, 162),
            (x + 15, 170)
        ]

        pygame.draw.polygon(
            pantalla,
            (255, 135, 45),
            puntos
        )

        pygame.draw.circle(
            pantalla,
            (255, 220, 100),
            (x, 160),
            7
        )


def dibujar_personaje(
    pantalla, rect, direccion=1
):

    x = rect.x
    y = rect.y

    # Piernas
    pygame.draw.rect(
        pantalla,
        (45, 50, 75),
        (x + 6, y + 35, 10, 20)
    )

    pygame.draw.rect(
        pantalla,
        (45, 50, 75),
        (x + 23, y + 35, 10, 20)
    )

    # Cuerpo
    pygame.draw.rect(
        pantalla,
        (170, 125, 85),
        (x + 5, y + 17, 29, 25),
        border_radius=5
    )

    # Cinturon
    pygame.draw.rect(
        pantalla,
        (70, 50, 45),
        (x + 5, y + 35, 29, 5)
    )

    # Cabeza
    pygame.draw.circle(
        pantalla,
        (230, 175, 130),
        (x + 19, y + 13),
        12
    )

    # Cabello
    pygame.draw.arc(
        pantalla,
        (45, 32, 40),
        (x + 7, y, 24, 22),
        math.pi,
        2 * math.pi,
        6
    )

    # Ojo segun direccion
    ojo_x = x + 24 if direccion == 1 else x + 14

    pygame.draw.circle(
        pantalla,
        (20, 20, 25),
        (ojo_x, y + 12),
        2
    )

    # Espada decorativa
    espada_x = x + 34 if direccion == 1 else x + 4

    pygame.draw.line(
        pantalla,
        (210, 215, 225),
        (espada_x, y + 25),
        (espada_x + direccion * 7, y + 47),
        4
    )
