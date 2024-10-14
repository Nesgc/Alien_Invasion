import sys
import pygame
from settings import Settings
from ship import Ship
from character import Character

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("alien invasion")
        
        self.ship = Ship(self)
        self.character = Character(self)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
                    
            
            self.clock.tick(60)

    def _check_events(self):
        """respond to keypresses and mouse events"""
         #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        #redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.character.blit_character()
                
        #make the most recently drawn screen visible
        pygame.display.flip()
    
if __name__ == '__main__':
    #make a game instance, and run the game
    ai=AlienInvasion()
    ai.run_game()