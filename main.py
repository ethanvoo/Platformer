import pygame
import sys

from Player import Player
from Platform import Platform
import Colors, Textures

class Game:
    def __init__(self, title: str, screen_width: int, screen_height: int):
        pygame.init()

        self.screen_width: int = screen_width
        self.screen_height: int = screen_height
        self.DEBUG_MODE: bool = False

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()

        self.player_texture = pygame.image.load(Textures.PLAYER).convert_alpha()
        self.player = Player(
            texture = self.player_texture, 
            init_x = 100, 
            init_y = 100,
            debug = self.DEBUG_MODE
        )

        self.platform_texture = pygame.image.load(Textures.PLATFORM).convert_alpha()
        self.platforms: list[Platform] = [
            Platform(
                texture = self.platform_texture, 
                init_x = 0, 
                init_y = self.screen_height - self.platform_texture.get_height(),
                debug = self.DEBUG_MODE
            ),
            Platform(
                texture = self.platform_texture, 
                init_x = 512, 
                init_y = self.screen_height - self.platform_texture.get_height() - self.platform_texture.get_height() * 2,
                debug = self.DEBUG_MODE
            )
        ]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            self.screen.fill(Colors.BLACK)

            self.player.check_movement()
            self.player.update_and_draw(self.screen, self.platforms)
            
            for platform in self.platforms:
                platform.update_and_draw(self.screen)

            

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game("Game", 1920, 1080)
    game.run()