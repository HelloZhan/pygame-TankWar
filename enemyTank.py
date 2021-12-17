import pygame
import random
import bulletClass
"""
修改时间：2021.12.15
修改人：2019051604048 詹孝东
模块描述：
该模块是敌方坦克类
该类组合了子弹类，因为坦克都有子弹嘛
敌方坦克类继承了pygame的精灵类，从而实现敌方坦克的相关功能 详情情况下方描述
"""
class EnemyTank(pygame.sprite.Sprite):
    def __init__(self, x=None, kind=None, isred=None):
        pygame.sprite.Sprite.__init__(self)

        # 坦克出现前动画是否播放
        self.flash = False
        self.times = 90

        # 参数:坦克种类
        self.kind = kind
        # 随机选择坦克的种类
        if not kind:
            self.kind = random.choice([1, 2, 3, 4])

        # 根据坦克的种类，加载不同种类坦克的图片
        if self.kind == 1:
            self.enemy_x_0 = pygame.image.load(r"image\enemy_1_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load(r"image\enemy_1_3.png").convert_alpha()
        if self.kind == 2:
            self.enemy_x_0 = pygame.image.load(r"image\enemy_2_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load(r"image\enemy_2_3.png").convert_alpha()
        if self.kind == 3:
            self.enemy_x_0 = pygame.image.load(r"image\enemy_3_1.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load(r"image\enemy_3_0.png").convert_alpha()
        if self.kind == 4:
            self.enemy_x_0 = pygame.image.load(r"image\enemy_4_0.png").convert_alpha()
            self.enemy_x_3 = pygame.image.load(r"image\enemy_4_3.png").convert_alpha()
        self.enemy_3_0 = pygame.image.load(r"image\enemy_3_0.png").convert_alpha()
        self.enemy_3_2 = pygame.image.load(r"image\enemy_3_2.png").convert_alpha()

        # 参数:是否携带道具
        self.isred = isred
        # 随机选择是否携带道具（5分之1的概率）
        if not None:
            self.isred = random.choice((True, False, False, False, False))
        # 如果携带道具则更新图片
        if self.isred:
            self.tank = self.enemy_x_3
        else:
            self.tank = self.enemy_x_0

        # 参数:坦克位置
        self.x = x
        # 随机选择坦克出现的位置（因为只有上方3个复活地）
        if not self.x:
            self.x = random.choice([1, 2, 3])
        self.x -= 1

        # 运动中的两种图片
        self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.rect = self.tank_R0.get_rect()
        # 设置位置
        self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 3 + 0 * 24

        # 坦克速度   方向   生命   子弹生命   子弹延迟
        self.speed = 1
        self.dir_x, self.dir_y = 0, 1
        self.life = 1
        self.bulletNotCooling = True
        self.bullet = bulletClass.Bullet()

        # 是否撞墙，撞墙则改变方向
        self.dirChange = False

        # 每种坦克不同的属性
        if self.kind == 2:
            self.speed = 3
        if self.kind == 3:
            self.life = 3
    # 射击子弹方法
    def shoot(self):
        # 赋予子弹生命 并调用方法改变相应图片
        self.bullet.life = True
        self.bullet.changeImage(self.dir_x, self.dir_y)

        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top + 1
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom - 1
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet.rect.left = self.rect.right + 1
            self.bullet.rect.top = self.rect.top + 20
    # 移动方法
    def move(self, tankGroup, brickGroup, ironGroup,riverGroup):
        # 进行移动
        self.rect = self.rect.move(self.speed * self.dir_x, self.speed * self.dir_y)
        # 选择相应图片（为啥是两张图片呢，subsurface是共享的 这样就是在移动中切换两种图片就会有移动效果）
        if self.dir_x == 0 and self.dir_y == -1:
            self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        elif self.dir_x == 0 and self.dir_y == 1:
            self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        elif self.dir_x == -1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        elif self.dir_x == 1 and self.dir_y == 0:
            self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
            self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))

        # 碰撞地图边缘（随机选择方向）
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        elif self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
        # 碰撞墙体 和坦克 和河流 （随机选择方向）
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None) \
                or pygame.sprite.spritecollide(self, tankGroup, False, None) \
                or pygame.sprite.spritecollide(self, riverGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.dir_x, self.speed * -self.dir_y)
            self.dir_x, self.dir_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
