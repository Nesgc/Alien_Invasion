import pygame

class Character:
    
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/thresh.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.center = self.screen_rect.center
        
    def blit_character(self):
        self.screen.blit(self.image,self.rect)