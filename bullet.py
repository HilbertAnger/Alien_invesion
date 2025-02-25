import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船发射的子弹"""

    def __init__(self,ai_game):
        """在飞船位置创建一个子弹"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #创建一个矩形再设置位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #浮点数表示子弹坐标
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        #更新子弹位置
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)