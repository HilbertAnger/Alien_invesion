import sys
import pygame
from settings import Settings

class AlienInvesion:
    """manage game action and resource"""
    def __init__(self):
        """init game and resource"""
        pygame.init()

        self.settings = Settings()

        #设置帧率
        self.clock = pygame.time.Clock()


        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监听键盘和鼠标
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #绘制窗口颜色
            self.screen.fill(self.settings.bg_color)

            # display the mode
            pygame.display.flip()
            #设置为60帧
            self.clock.tick(self.settings.clock_tick)

if __name__ == '__main__':
    # create and run the game
    ai = AlienInvesion()
    ai.run_game()
