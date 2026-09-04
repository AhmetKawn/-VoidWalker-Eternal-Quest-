import pygame
  from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_BLACK
  from src.entities.player import Player
  from src.entities.enemies.slime import Slime
  from src.world.map_manager import MapManager
  from src.ui.hud import HUD

  class Game:
      def __init__(self):
          self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
          pygame.display.set_caption("Aetheria: The Shifting Realms")
          self.clock = pygame.time.Clock()
          self.running = True

          # Sistemleri Başlat
          self.map_manager = MapManager()
          self.player = Player(self)
          self.hud = HUD(self)
          self.enemies = [Slime(self) for _ in range(5)]

      def run(self):
          while self.running:
              self._handle_events()
              self._update()
              self._draw()
              self.clock.tick(FPS)

      def _handle_events(self):
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  self.running = False

      def _update(self):
          self.player.update()
          for enemy in self.enemies:
              enemy.update()
          self.map_manager.update()

      def _draw(self):
          self.screen.fill(COLOR_BLACK)

          self.map_manager.draw(self.screen)
          for enemy in self.enemies:
              enemy.draw(self.screen)
          self.player.draw(self.screen)
          self.hud.draw(self.screen)

          pygame.display.flip()
