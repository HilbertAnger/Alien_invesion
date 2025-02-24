import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船并设置初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取矩阵
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        #将飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.settings = ai_game.settings

        #移动标志
        self.moving_right = False
        self.moving_left = False

        # 另存一个变量x将飞船坐标改为浮点数
        self.x = float(self.rect.x)

    def upgrade(self):
        """控制移动"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        #再将变量赋予飞船的坐标
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)