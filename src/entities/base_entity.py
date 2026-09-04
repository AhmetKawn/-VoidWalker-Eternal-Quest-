 import pygame
  from src.constants import COLOR_WHITE

  class BaseEntity:
      def __init__(self, game, x, y, width, height, color=COLOR_WHITE):
          self.game = game
          self.rect = pygame.Rect(x, y, width, height)
          self.color = color

      def draw(self, screen):
          pygame.draw.rect(screen, self.color, self.rect, border_radius=5)

      def update(self):
          pass

  src/entities/player.py

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

  src/entities/enemies/slime import slime.py

  (Klasör: src/entities/enemies/slime.py)
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
