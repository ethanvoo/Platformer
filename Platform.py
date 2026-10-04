from pygame import Rect, Surface
import pygame

import Colors
class Platform:
    def __init__(
            self,
            texture: Surface, 
            init_x: int, 
            init_y: int,
            debug: bool = False
    ):
        self.texture: Surface = texture
        self.x: int = init_x
        self.y: int = init_y
        self.width: int = texture.get_width()
        self.height: int = texture.get_height()

        self.debug: bool = debug

        self.hitbox: Rect = Rect(self.x, self.y, self.width, self.height)

    def __draw(self, screen: Surface) -> None:
        screen.blit(self.texture, (self.x, self.y))

        if self.debug:
            pygame.draw.rect(screen, Colors.WHITE, self.hitbox, 2)

    def update_and_draw(self, screen: Surface) -> None:
        self.__draw(screen)
