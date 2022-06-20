import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
  #Initialize game and create a screen object
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")

  #Make a ship
  ship = Ship(screen)


  #Starts the main loop of the game.
  while True:

    #checks for keybooard and mouse movements
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    #redaws screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make the most recently drawn visible
    pygame.display.flip()
  
run_game()