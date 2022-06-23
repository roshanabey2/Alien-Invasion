import sys

import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
      # Move the ship to the right.
      ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      #moves ship to the left.
      ship.moving_left = True
    elif event.key == pygame.K_SPACE:
      #Create a new bullet and adds it to the bullet group
      new_bullet = Bullet(ai_settings, screen, ship)
      bullets.add(new_bullet)

def check_keyup_events(event, ship):   
  if event.type ==pygame.KEYUP:
      #stops the ship from moving in either direction
    if event.key == pygame.K_RIGHT:
      ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      ship.moving_left = False


def check_events(ship, ai_settings, ship, bullets):
  """Respond to keypresses and mouse events."""
  #checks for keybooard and mouse movements
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ai_settings, ship, bullets)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)
        


def update_screen(ai_settings, screen, ship, bullets):
    
    #redraws screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    #Redraw all bullets behind ship and aliens
    ship.blitme()
    
    # Make the most recently drawn visible
    pygame.display.flip()
  