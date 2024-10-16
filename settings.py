class Settings:
    """a class to store all settings for alien invasion"""
    
    def __init__(self):
        """initialize the games settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height=800
        self.bg_color = (176,224,230)
        
        self.ship_speed = 5
        self.ship_limit = 3
        
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        
        self.alien_speed = 10.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 its left
        self.fleet_direction = 1
        