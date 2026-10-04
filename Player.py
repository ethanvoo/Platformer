import pygame
from pygame import Surface, Rect

from Platform import Platform

import Colors

class Player:
    def __init__(
            self, 
            texture: Surface, 
            init_x: int, 
            init_y: int,
            player_speed: int = 5, 
            mass: float = 1.0,
            debug: bool = False
    ):
        self.x: int = init_x
        self.y: int = init_y
        self.width: int = texture.get_width()
        self.height: int = texture.get_height()
        self.texture: Surface = texture

        self.player_speed: int = player_speed
        self.gravity: float = 0.5
        self.mass: float = mass
        self.downward_velocity: float = 0.0
        self.direction: str = "stoped"
        self.on_ground: bool = True

        

        self.hitbox: Rect = Rect(self.x, self.y, self.width, self.height)

        self.debug: bool = debug

    def __draw(self, screen: Surface) -> None:
        screen.blit(self.texture, (self.x, self.y))

        if self.debug:
            pygame.draw.rect(screen, Colors.WHITE, self.hitbox, 2)

    def __apply_gravity(self) -> None:
        self.on_ground = False
        if self.mass > 0:
            gravity_force = self.mass * self.gravity
            acceleration = gravity_force / self.mass
            self.downward_velocity += acceleration
            self.y += round(self.downward_velocity)
            self.hitbox.topleft = (self.x, self.y)

    def update_and_draw(self, screen: Surface, platforms: list[Platform]) -> None:
        self.__apply_gravity()
        
        for platform in platforms:
            if self.check_collision(platform.hitbox):
                collision_side = self.check_collision_side(platform.hitbox)
                if collision_side == "top":
                    self.downward_velocity = 0.0
                    self.on_ground = True
                if collision_side == "bottom":
                    self.downward_velocity = 0.0
                    self.y = platform.hitbox.bottom
                if collision_side == "left":
                    self.x = platform.hitbox.left - self.width
                if collision_side == "right":
                    self.x = platform.hitbox.right
                    
                break


        
        

        self.hitbox.topleft = (self.x, self.y)
        self.__draw(screen)

    def check_movement(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.player_speed
        if keys[pygame.K_d]:
            self.x += self.player_speed
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.on_ground:
            self.downward_velocity = -10.0

    def check_collision(self, other_rect: Rect) -> bool:
        return self.hitbox.colliderect(other_rect)

    def check_collision_side(self, other_rect: Rect) -> str:
        if not self.hitbox.colliderect(other_rect):
            return "none"

        # How far the player is sunk into the platform from each direction
        overlap_top    = self.hitbox.bottom - other_rect.top      # player landing on top
        overlap_bottom = other_rect.bottom - self.hitbox.top      # player hitting head
        overlap_left   = self.hitbox.right - other_rect.left      # player hitting platform's left side
        overlap_right  = other_rect.right - self.hitbox.left      # player hitting platform's right side

        smallest = min(overlap_top, overlap_bottom, overlap_left, overlap_right)

        if smallest == overlap_top:
            return "top"
        elif smallest == overlap_bottom:
            return "bottom"
        elif smallest == overlap_left:
            return "left"
        else:
            return "right"

        

    


