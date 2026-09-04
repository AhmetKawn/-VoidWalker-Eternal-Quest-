 import pygame
  import random
  from src.entities.base_entity import BaseEntity
  from src.constants import ENEMY_SPEED, COLOR_ENEMY

  class Slime(BaseEntity):
      def __init__(self, game):
          x = random.randint(0, 1000)
          y = random.randint(0, 700)
          super().__init__(game, x, y, 30, 30, COLOR_ENEMY)

      def update(self):
          # Basit Yapay Zeka: Oyuncuyu takip et
          player_rect = self.game.player.rect
          if self.rect.x < player_rect.x: self.rect.x += ENEMY_SPEED
          elif self.rect.x > player_rect.x: self.rect.x -= ENEMY_SPEED

          if self.rect.y < player_rect.y: self.rect.y += ENEMY_SPEED
          elif self.rect.y > player_rect.y: self.rect.y -= ENEMY_SPEED
