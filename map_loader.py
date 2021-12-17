# -*- coding: utf-8 -*-
import pygame
import sys
import maps
"""
修改时间：2021.12.15
修改人：2019051604048 詹孝东
模块描述：
该模块是地图建造类 聚合了地图类 如果建造完成会返回一个列表（游戏类可以拿着列表给地图类生成地图）
该类与游戏类的结构相差不大（只不过只有地图类的参与）
详细情况情况下方代码
"""
# 此类是地图建造类 可以实时显示地图 并将地图创建为数组返回
class Map_loader:
    # 初始化函数
    def __init__(self):
        pygame.init()
        # 用于加载和播放声音的 pygame 模块
        pygame.mixer.init()
        resolution = 750, 630
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption("Build a map")

        self.clock = pygame.time.Clock()
        # 加载图片-----------------------------------------------------------------------------
        self.background_image = pygame.image.load(r"image\background.png")
        self.background_image_tishi = pygame.image.load(r"image\background_maploader_tishi.png")
        self.select_image = pygame.image.load(r"image\select.png")

        # 敌方出现的图片
        appearance_image = pygame.image.load(r"image\special_effects\appear.png").convert_alpha()
        self.appearance = appearance_image.subsurface((96, 0), (48, 48))

        # 玩家一和玩家二的图片
        tank_L1_image = pygame.image.load(r"image\tank_T1_0.png").convert_alpha()
        tank_L2_image = pygame.image.load(r"image\tank_T2_0.png").convert_alpha()

        self.tank_l1 = tank_L1_image.subsurface((0, 0), (48, 48))
        self.tank_l2 = tank_L2_image.subsurface((0, 0), (48, 48))
        self.tank_l2_bottom = tank_L2_image.subsurface((0, 48), (48, 48))

        # 参数-------------------------------------------------------------------------------
        self.moving = 0
        self.movdir = 0
        # 创建地图并传出
        self.map_num = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        # 现在选择的位置
        self.now_x, self.now_y = 2, 0
        # 是正常模式还是单挑模式
        self.is_normal_mode = True

    # 因为单挑模式没有家和敌方坦克 且坦克初始位置也不同 所有需要两个判断方法
    # 判断位置合法性的函数（普通模式版）--------------------------------------
    # 功能：返回当前位置是否合法
    def judgment_is_legal_normal_mode(self) -> bool:
        if self.now_x in [0,1] and self.now_y in [0,1,12,13,24,25]:
            return False
        if self.now_x in [24,25] and self.now_y in [8,9,12,13,16,17]:
            return False
        return True

    # 判断位置合法性的函数（单挑模式版）--------------------------------------
    # 功能：返回当前位置是否合法
    def judgment_is_legal_singled_out(self) -> bool:
        if self.now_x in [0,1] and self.now_y in [12,13]:
            return False
        if self.now_x in [24,25] and self.now_y in [12,13]:
            return False
        return True

    # 由于不同模式的坦克位置等不同所有需要两个不同的执行函数
    # 普通版本的函数
    def normal_mode(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_0] or key_pressed[pygame.K_KP0]:
            if self.judgment_is_legal_normal_mode():
                self.map_num[self.now_x][self.now_y] = 0
        elif key_pressed[pygame.K_1] or key_pressed[pygame.K_KP1]:
            if self.judgment_is_legal_normal_mode():
                self.map_num[self.now_x][self.now_y] = 1
        elif key_pressed[pygame.K_2] or key_pressed[pygame.K_KP2]:
            if self.judgment_is_legal_normal_mode():
                self.map_num[self.now_x][self.now_y] = 2
        elif key_pressed[pygame.K_3] or key_pressed[pygame.K_KP3]:
            if self.judgment_is_legal_normal_mode():
                self.map_num[self.now_x][self.now_y] = 3
        elif key_pressed[pygame.K_4] or key_pressed[pygame.K_KP4]:
            if self.judgment_is_legal_normal_mode():
                self.map_num[self.now_x][self.now_y] = 4
        elif key_pressed[pygame.K_5] or key_pressed[pygame.K_KP5]:
            if self.judgment_is_legal_normal_mode():
                self.map_num[self.now_x][self.now_y] = 5

        # 画背景
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.background_image_tishi, (630, 0))

        # 画敌军出现位置
        self.screen.blit(self.appearance, (3, 3))
        self.screen.blit(self.appearance, (3 + 24 * 12, 3))
        self.screen.blit(self.appearance, (3 + 24 * 24, 3))

        # 画我方坦克
        self.screen.blit(self.tank_l1, (3 + 8 * 24, 3 + 24 * 24))
        self.screen.blit(self.tank_l2, (3 + 16 * 24, 3 + 24 * 24))

    # 单挑版本的函数
    def singled_out(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_0] or key_pressed[pygame.K_KP0]:
            if self.judgment_is_legal_singled_out():
                self.map_num[self.now_x][self.now_y] = 0
        elif key_pressed[pygame.K_1] or key_pressed[pygame.K_KP1]:
            if self.judgment_is_legal_singled_out():
                self.map_num[self.now_x][self.now_y] = 1
        elif key_pressed[pygame.K_2] or key_pressed[pygame.K_KP2]:
            if self.judgment_is_legal_singled_out():
                self.map_num[self.now_x][self.now_y] = 2
        elif key_pressed[pygame.K_3] or key_pressed[pygame.K_KP3]:
            if self.judgment_is_legal_singled_out():
                self.map_num[self.now_x][self.now_y] = 3
        elif key_pressed[pygame.K_4] or key_pressed[pygame.K_KP4]:
            if self.judgment_is_legal_singled_out():
                self.map_num[self.now_x][self.now_y] = 4
        elif key_pressed[pygame.K_5] or key_pressed[pygame.K_KP5]:
            if self.judgment_is_legal_singled_out():
                self.map_num[self.now_x][self.now_y] = 5

        # 画背景
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.background_image_tishi, (630, 0))

        # 画我方坦克
        self.screen.blit(self.tank_l1, (3 + 12 * 24, 3 + 24 * 24))
        self.screen.blit(self.tank_l2_bottom, (3 + 12 * 24, 3 + 0 * 24))

    # 运行函数
    def function(self,is_normal_mode):
        # 是否是单挑模式
        self.is_normal_mode = is_normal_mode
        # 循环体
        while True:
            # 创建地图
            bgMap = maps.Map()
            # 根据模式不同 选择的地图初始化不同
            if is_normal_mode:
                bgMap.checkpoint(99, self.map_num)
            else:
                bgMap.checkpoint(88, self.map_num)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            key_pressed = pygame.key.get_pressed()
            # 如果按下回车进入游戏
            if key_pressed[pygame.K_p]:
                return self.map_num
            # 如果按下esc返回
            if key_pressed[pygame.K_ESCAPE]:
                return 0
            # 按r进行初始化
            if key_pressed[pygame.K_r]:
                self.__init__()
                self.is_normal_mode = is_normal_mode

            if self.moving:
                self.moving -= 1
                if self.movdir == 0 and self.moving == 0 and self.now_x > 0:
                    self.now_x -= 1

                if self.movdir == 1 and self.moving == 0 and self.now_x < 25:
                    self.now_x += 1

                if self.movdir == 2 and self.moving == 0 and self.now_y > 0:
                    self.now_y -= 1

                if self.movdir == 3 and self.moving == 0 and self.now_y < 25:
                    self.now_y += 1

            if not self.moving:
                if key_pressed[pygame.K_w] or key_pressed[pygame.K_UP]:
                    self.moving = 12
                    self.movdir = 0
                elif key_pressed[pygame.K_s] or key_pressed[pygame.K_DOWN]:
                    self.moving = 12
                    self.movdir = 1
                elif key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
                    self.moving = 12
                    self.movdir = 2
                elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
                    self.moving = 12
                    self.movdir = 3

            if is_normal_mode:
                self.normal_mode()
            else:
                self.singled_out()

            # 画砖块
            for each in bgMap.brickGroup:
                self.screen.blit(each.image, each.rect)
            # 画石头
            for each in bgMap.ironGroup:
                self.screen.blit(each.image, each.rect)
            # 画河流
            for each in bgMap.riverGroup:
                self.screen.blit(each.image, each.rect)
            # 画冰面
            for each in bgMap.iceGroup:
                self.screen.blit(each.image, each.rect)
            # 画树
            for each in bgMap.treeGroup:
                self.screen.blit(each.image, each.rect)
            # 画home
            for each in bgMap.homeGroup:
                self.screen.blit(each.image, each.rect)

            self.screen.blit(self.select_image, (3 + self.now_y * 24, 3 + self.now_x * 24))
            pygame.display.flip()
            self.clock.tick(60)
