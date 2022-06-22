import pygame

class Ship():
  def __init__(self, ai_settings, screen):
    """Initialize the ship and set its star ting position"""
    self.screen = screen
    self.ai_settings = ai_settings

    #Load the ship image and get it to react.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # Start each new ship at the bottom center
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    #stores a decimal value for the ship's center
    self.center = float(self.rect.centerx)

    #Movement Flag
    self.moving_right = False
    self.moving_left = False

  def update(self):
    """Update the ship's position based on the movement flag"""
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.rect.center += self.ai_settings.ship_speed_factor
    elif self.moving_left and seld.rect.left > 0:
      self.rect.center -= self.ai_settings.ship_speed_factor

    # Update rect object from self.center
    self.rect.centerx = self.center


  def blitme(self):
    """Draw the ship at its current location""" 
    self.screen.blit(self.image, self.rect)
  
