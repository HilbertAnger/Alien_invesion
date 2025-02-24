import sys
import pygame
from settings import Settings
from ship import Ship

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

        self.ship = Ship(self)# 在Ship类里调用了上边self.screen，所以需要位于它的下边

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.upgrade()
            self._upgrade_screen()

            #设置为60帧
            self.clock.tick(self.settings.clock_tick)

    def _check_events(self):
        """监查按键和鼠标"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self,event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            # Right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # Quit
            sys.exit()

    def _check_keyup_event(self,event):
        """响应释放"""

        if event.key == pygame.K_RIGHT:
            # Right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Left
            self.ship.moving_left = False

    def _upgrade_screen(self):
        """更新显示"""
        # 每次循环时都重绘需要显示的
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # display the mode
        pygame.display.flip()

if __name__ == '__main__':
    # create and run the game
    ai = AlienInvesion()
    ai.run_game()
