import sys
import pygame

class Keys:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,1000))
        self.bg_color = (176,224,230)
        
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
    
if __name__ == '__main__':
    #make a game instance, and run the game
    ai=Keys()
    ai.run_game()