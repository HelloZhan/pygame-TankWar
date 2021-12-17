import pygame
import bulletClass
"""
修改时间：2021.12.15
修改人：2019051604048 詹孝东
模块描述：
该模块是我方坦克类继承了pygame的精灵类，从而实现了相关功能
该类组合了子弹类，有射出子弹方法、升级、降级、移动方法
详细情况情况下方代码
"""
# 玩家一和玩家二的坦克图片
tank_T1_0 = r"image\tank_T1_0.png"
tank_T1_1 = r"image\tank_T1_1.png"
tank_T1_2 = r"image\tank_T1_2.png"
tank_T2_0 = r"image\tank_T2_0.png"
tank_T2_1 = r"image\tank_T2_1.png"
tank_T2_2 = r"image\tank_T2_2.png"

# 我方坦克类（继承了pygame的精灵类）
class MyTank(pygame.sprite.Sprite):
    def __init__(self, playerNumber):
        pygame.sprite.Sprite.__init__(self)

        # 玩家生命
        self.life = True

        # 根据是玩家一还是玩家二进行选择图片
        if playerNumber == 1:
            self.tank_L0_image = pygame.image.load(tank_T1_0).convert_alpha()
            self.tank_L1_image = pygame.image.load(tank_T1_1).convert_alpha()
            self.tank_L2_image = pygame.image.load(tank_T1_2).convert_alpha()
        if playerNumber == 2:
            self.tank_L0_image = pygame.image.load(tank_T2_0).convert_alpha()
            self.tank_L1_image = pygame.image.load(tank_T2_1).convert_alpha()
            self.tank_L2_image = pygame.image.load(tank_T2_2).convert_alpha()
        # 初始坦克为0级
        self.level = 0
        self.tank = self.tank_L0_image

        # 运动中的两种图片
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))

        self.rect = self.tank_R0.get_rect()

        # 根据玩家不同放置位置也不同
        if playerNumber == 1:
            self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
        if playerNumber == 2:
            self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24

        # 坦克速度   坦克方向   坦克生命   子弹冷却
        self.speed = 3
        self.dir_x, self.dir_y = 0, -1
        self.life = 3
        self.bulletNotCooling = True
        self.bullet = bulletClass.Bullet()

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
        # 根据等级不同 子弹速度和是否加强也不同
        if self.level == 1:
            self.bullet.speed = 16
            self.bullet.strong = False
        if self.level == 2:
            self.bullet.speed = 16
            self.bullet.strong = True
        if self.level == 3:
            self.bullet.speed = 48
            self.bullet.strong = True

    # 升级
    def levelUp(self):
        if self.level < 2:
            self.level += 1
        if self.level == 0:
            self.tank = self.tank_L0_image
        if self.level == 1:
            self.tank = self.tank_L1_image
        if self.level == 2:
            self.tank = self.tank_L2_image
        if self.level == 3:
            self.tank = self.tank_L2_image
    # 降级
    def levelDown(self):
        if self.level > 0:
            self.level -= 1
        if self.level == 0:
            self.tank = self.tank_L0_image
            self.bullet.speed = 6
            self.bullet.strong = False
        if self.level == 1:
            self.tank = self.tank_L1_image
        if self.level == 2:
            self.tank = self.tank_L2_image

    # 返回True 代表发生碰撞
    # 碰撞检测并移动
    def moveUp(self, tankGroup, brickGroup, ironGroup,riverGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        # 产生移动的感觉
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        self.dir_x, self.dir_y = 0, -1
        # 检测是否移动边界
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        # 检测是否和砖块、石块、河流阻挡
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None)\
                or pygame.sprite.spritecollide(self, riverGroup,False,None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        # 检测是否和其它坦克所阻挡
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        return False

    def moveDown(self, tankGroup, brickGroup, ironGroup,riverGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.dir_x, self.dir_y = 0, 1
        if self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None)\
                or pygame.sprite.spritecollide(self, riverGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        return False

    def moveLeft(self, tankGroup, brickGroup, ironGroup,riverGroup):
        self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        self.dir_x, self.dir_y = -1, 0
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None)\
                or pygame.sprite.spritecollide(self, riverGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        return False

    def moveRight(self, tankGroup, brickGroup, ironGroup,riverGroup):
        self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))
        self.dir_x, self.dir_y = 1, 0
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None) \
                or pygame.sprite.spritecollide(self, riverGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        return False