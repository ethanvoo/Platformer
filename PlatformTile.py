import pygame
from pygame import Rect, Surface
from TilePosition import TilePosition

import Colors

class PlatformTile:
    def __init__(self, texture: Surface, x: int, y: int, tile_position: TilePosition, debug: bool = False):
        self.x: int = x
        self.y: int = y
        self.texture: Surface = texture
        self.tile_position: TilePosition = tile_position
        self.debug: bool = debug

        self.width: int = texture.get_width()
        self.height: int = texture.get_height()

        self.hitbox: Rect = Rect(self.x, self.y, self.width, self.height)

    def __draw(self, screen: Surface) -> None:
        screen.blit(self.texture, (self.x, self.y))

        if self.debug:
            pygame.draw.rect(screen, Colors.WHITE, self.hitbox, 2)
    
    def update_and_draw(self, screen: Surface) -> None:
        self.__draw(screen)


