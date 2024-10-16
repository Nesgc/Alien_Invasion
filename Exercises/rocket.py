import sys
import pygame

class Rocket:
    
    def __init__(self):
        pygame.init()
        
        self.screen=pygame.display.set_mode((1200,800))
        self.screen_rect = self.screen.get_rect()
        
        #load the ship image and get its rect 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        #start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        

        
        self.bg_color = (176,224,230)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.moving_left = False
                    elif event.key == pygame.K_UP:
                        self.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.moving_down = False

            self.update()
            self._update_screen()


           
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 2
        if self.moving_left and self.rect.left > 0:
            self.x -= 2
            
            # Move up if the ship is not at the top edge
        if self.moving_up and self.rect.top > 0:
            self.y -= 2
        # Move down if the ship is not at the bottom edge
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 2  
        
        self.rect.x = self.x
        self.rect.y = self.y
        
    def _update_screen(self):
        #redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.blitme()
                
        #make the most recently drawn screen visible
        pygame.display.flip()
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
if __name__ == '__main__':
    #make a game instance, and run the game
    ai=Rocket()
    ai.run_game()