import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """alien"""

    def __init__(self,ai_game):
        """初始化外星人并设置初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #加载图像并创建矩阵
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人都初始化在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的精确水平位置
        self.x = float(self.rect.x)


    def check_edges(self):
        """如果外星人位于屏幕边缘就返回True"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """move to right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x