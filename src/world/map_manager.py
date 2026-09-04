import pygame
  from src.constants import COLOR_GRASS, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

  class MapManager:
      def __init__(self):
          # Basit bir ızgara sistemi
          self.grid = []
          for x in range(0, SCREEN_WIDTH, TILE_SIZE):
              row = []
              for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
                  row.append(COLOR_GRASS)
              self.grid.append(row)

      def update(self):
          pass

      def draw(self, screen):
          for i in range(len(self.grid)):
              for j in range(len(self.grid[0])):
                  pygame.draw.rect(screen, self.grid[i][j],
                                   (i*TILE_SIZE, j*TILE_SIZE, TILE_SIZE-1, TILE_SIZE-1))

  src/ui/hud.py

  import pygame
  from src.constants import COLOR_UI_BG, COLOR_WHITE, COLOR_GOLD

  class HUD:
      def __init__(self, game):
          self.game = game
          self.font = pygame.font.SysFont("Arial", 24, bold=True)

      def draw(self, screen):
          # Panel arka planı
          overlay = pygame.Surface((250, 80), pygame.SRCALPHA)
          overlay.fill(COLOR_UI_BG)
          screen.blit(overlay, (10, 10))

          # Yazılar
          hp_text = self.font.render(f"HP: {self.game.player.hp}", True, COLOR_WHITE)
          gold_text = self.font.render(f"Gold: {self.game.player.gold}", True, COLOR_GOLD)

          screen.blit(hp_text, (20, 20))
          screen.blit(gold_text, (20, 45))
