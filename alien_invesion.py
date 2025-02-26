import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.upgrade()
            self._update_bullets()
            self._update_aliens()

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
        elif event.key == pygame.K_SPACE:
            #bullet
            self._fire_bullet()
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

    def _fire_bullet(self):
        """创建一颗子弹并加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """更新子弹并删除屏幕外子弹"""
        #更新子弹位置
        self.bullets.update()

        # 删除屏幕外子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))检验子弹是否消失

    def _create_fleet(self):
        """创建外星人编队"""
        #创建一个外星人,不断添加，直到没有空间
        #外星人的间距为外星人的宽度
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x = alien_width
        current_y = alien_height
        while current_y < self.settings.screen_height - 3 * alien_height:
            while current_x < self.settings.screen_width - 2 * alien_width:
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width

            #一行完成后重置x并递增y
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self,x_position,y_position):
        #创建一个外星人并放在当前行
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """在有外星人靠近边缘时采取措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """move dowm and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_aliens(self):
        """update aliens"""
        self._check_fleet_edges()
        self.aliens.update()



    def _upgrade_screen(self):
        """更新显示"""
        # 每次循环时都重绘需要显示的
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()

        self.aliens.draw(self.screen)

        # display the mode
        pygame.display.flip()


if __name__ == '__main__':
    # create and run the game
    ai = AlienInvesion()
    ai.run_game()
