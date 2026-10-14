
import pygame

from settings import (
    ANCHO,
    ALTO,
    VELOCIDAD_JUGADOR,
    FUERZA_SALTO,
    GRAVEDAD,
    DORADO
)


class Jugador(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # Apariencia provisional del personaje
        self.image = pygame.Surface(
            (38, 55),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            self.image,
            DORADO,
            (0, 0, 38, 55),
            border_radius=8
        )

        # Ojos
        pygame.draw.circle(
            self.image,
            (20, 20, 30),
            (26, 15),
            4
        )

        self.rect = self.image.get_rect(
            topleft=(x, y)
        )

        # Movimiento
        self.velocidad_y = 0
        self.en_suelo = False
        self.direccion = 1

    def actualizar(self, plataformas):

        teclas = pygame.key.get_pressed()

        
        # Velocidad normal y velocidad al correr
        velocidad_actual = VELOCIDAD_JUGADOR

        if teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]:
            velocidad_actual = VELOCIDAD_JUGADOR * 1.5

        movimiento_x = 0

        # Movimiento horizontal
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            movimiento_x = -velocidad_actual

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            movimiento_x = velocidad_actual


        # Saltar
        if (
            teclas[pygame.K_SPACE]
            or teclas[pygame.K_UP]
            or teclas[pygame.K_w]
        ) and self.en_suelo:

            self.velocidad_y = FUERZA_SALTO
            self.en_suelo = False

        # Movimiento horizontal y colisiones
        
        if movimiento_x > 0:
            self.direccion = 1

        elif movimiento_x < 0:
            self.direccion = -1

        self.rect.x += movimiento_x

        for plataforma in plataformas:
            if self.rect.colliderect(plataforma):

                if movimiento_x > 0:
                    self.rect.right = plataforma.left

                elif movimiento_x < 0:
                    self.rect.left = plataforma.right

        # Aplicar gravedad
        self.velocidad_y += GRAVEDAD
        self.velocidad_y = min(
            self.velocidad_y, 15
        )

        self.rect.y += round(self.velocidad_y)
        self.en_suelo = False

        # Colisiones verticales
        for plataforma in plataformas:

            if self.rect.colliderect(plataforma):

                if self.velocidad_y > 0:
                    self.rect.bottom = plataforma.top
                    self.en_suelo = True

                elif self.velocidad_y < 0:
                    self.rect.top = plataforma.bottom

                self.velocidad_y = 0

        # Limites horizontales
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

      
    def dibujar(self, pantalla):

        from graphics import dibujar_personaje

        dibujar_personaje(
            pantalla,
            self.rect,
            self.direccion
        )

