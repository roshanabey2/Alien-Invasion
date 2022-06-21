import sys

import pygame

def check_events(ship):
  """Respond to keypresses and mouse events."""
  #checks for keybooard and mouse movements
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
      elif event.key == pygame.K_LEFT:
        #moves ship to the left.
        ship.moving_left = True
    
    elif event.type ==pygame.KEYUP:
      #stops the ship from moving in either direction
      if event.key == pygame.K_RIGHT:
        ship.moving_right = False
      elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        


def update_screen(ai_settings, screen, ship):
    
    #redraws screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make the most recently drawn visible
    pygame.display.flip()
  