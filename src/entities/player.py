 import pygame
  from src.entities.base_entity import BaseEntity
  from src.constants import PLAYER_SPEED, COLOR_PLAYER

  class Player(BaseEntity):
      def __init__(self, game):
          super().__init__(game, 512, 384, 40, 40, COLOR_PLAYER)
          self.hp = 100
          self.gold = 0

      def update(self):
          keys = pygame.key.get_pressed()
          dx, dy = 0, 0

          if keys[pygame.K_a]: dx = -PLAYER_SPEED
          if keys[pygame.K_d]: dx = PLAYER_SPEED
          if keys[pygame.K_w]: dy = -PLAYER_SPEED
          if keys[pygame.K_s]: dy = PLAYER_SPEED

          self.rect.x += dx
          self.rect.y += dy

      def draw(self, screen):
          super().draw(screen)
          # Oyuncunun üzerine küçük bir "baş" çizelim
          pygame.draw.circle(screen, (255, 255, 255), self.rect.center, 5)
