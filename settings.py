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
        self.ship_speed = 3
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed = 3.0
        self.fleet_drop_speed = 10
        #fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1