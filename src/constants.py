import pygame

  # Ekran Ayarları
  SCREEN_WIDTH = 1024
  SCREEN_HEIGHT = 768
  FPS = 60

  # Renkler
  COLOR_BLACK = (20, 20, 25)
  COLOR_WHITE = (240, 240, 240)
  COLOR_PLAYER = (50, 150, 255)
  COLOR_ENEMY = (255, 80, 80)
  COLOR_GRASS = (34, 139, 34)
  COLOR_WALL = (80, 80, 80)
  COLOR_UI_BG = (40, 40, 50, 180)
  COLOR_GOLD = (255, 215, 0)

  # Oyun Mekanikleri
  PLAYER_SPEED = 5
  ENEMY_SPEED = 2
  TILE_SIZE = 64

  main.py

  import pygame
  import sys
  from src.core.game_loop import Game

  def main():
      pygame.init()
      # Oyun motorunu başlat
      game = Game()
      game.run()
      pygame.quit()
      sys.exit()

  if __name__ == "__main__":
      main()
