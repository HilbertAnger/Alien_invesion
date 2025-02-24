import pygame

class Settings:
    """存储设置"""
    def __init__(self):
        """初始化游戏设置"""
        self.caption = 'Alien Invesion'
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.clock_tick = 60

        #speed,使用小数会导致左右移动速度不同
        self.ship_speed = 2.5
