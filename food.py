import pygame
import random
"""
修改时间：2021.12.15
修改人：2019051604048 詹孝东
模块描述：
该模块是道具类
道具类继承了pygame的精灵类，从而实现道具的相关功能 详情情况下方描述
"""
# 此类为道具类 里面包含7种道具的类（继承了pygame的精灵类）
class Food(pygame.sprite.Sprite):
    def __init__(self):
        # 加载每个道具的图片
        self.food_boom = pygame.image.load(r"image\food\food_boom.png").convert_alpha()
        self.food_clock = pygame.image.load(r"image\food\food_clock.png").convert_alpha()
        self.food_gun = pygame.image.load(r"image\food\food_gun.png").convert_alpha()
        self.food_iron = pygame.image.load(r"image\food\food_iron.png").convert_alpha()
        self.food_protect = pygame.image.load(r"image\food\food_protect.png").convert_alpha()
        self.food_star = pygame.image.load(r"image\food\food_star.png").convert_alpha()
        self.food_tank = pygame.image.load(r"image\food\food_tank.png").convert_alpha()
        # 随机选择一个道具
        self.kind = random.choice([1,2,3,4,5,6,7])
        # 根据选择的道具加载对应道具的图片
        if self.kind ==1:
            self.image = self.food_boom
        elif self.kind == 2:
            self.image = self.food_clock
        elif self.kind == 3:
            self.image = self.food_gun
        elif self.kind == 4:
            self.image = self.food_iron
        elif self.kind == 5:
            self.image = self.food_protect
        elif self.kind == 6:
            self.image = self.food_star
        elif self.kind == 7:
            self.image = self.food_tank

        # 随机选择位置发放道具
        self.rect = self.image.get_rect()
        self.rect.left = self.rect.top = random.randint(100,500)
        # 首先将其生命为否（不显示） 当需要时将其置为true
        self.life = False

    # 改变道具发放的位置和道具类型（当需要更新道具执行此方法）
    def change(self):
        # 随机道具类型
        self.kind = random.choice([1, 2, 3, 4, 5, 6, 7])
        if self.kind == 1:
            self.image = self.food_boom
        elif self.kind == 2:
            self.image = self.food_clock
        elif self.kind == 3:
            self.image = self.food_gun
        elif self.kind == 4:
            self.image = self.food_iron
        elif self.kind == 5:
            self.image = self.food_protect
        elif self.kind == 6:
            self.image = self.food_star
        elif self.kind == 7:
            self.image = self.food_tank
        # 随机道具位置
        self.rect.left = self.rect.top = random.randint(100, 500)
        # 显示道具
        self.life = True
