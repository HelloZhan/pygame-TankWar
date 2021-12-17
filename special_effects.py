import pygame
"""
修改时间：2021.12.15
修改人：2019051604048 詹孝东
模块描述：
该模块是特性类，主要就是初始化图片，然后游戏类调用不同的方法显示不同的特效
因为特效的图片比较多 所有用列表保存所有的图片更好使用
详细情况情况下方代码
"""
# 特效的类
class SE:
    def __init__(self):

        # 初始化保护罩的图片
        protect_image = pygame.image.load(r"image\special_effects\protect.png").convert_alpha()
        self.protect = []
        self.protect.append(protect_image.subsurface((0, 0), (48, 48)))
        self.protect.append(protect_image.subsurface((48, 0), (48, 48)))

        # 敌军坦克出现动画
        appearance_image = pygame.image.load(r"image\special_effects\appear.png").convert_alpha()
        self.appearance = []
        self.appearance.append(appearance_image.subsurface((0, 0), (48, 48)))
        self.appearance.append(appearance_image.subsurface((48, 0), (48, 48)))
        self.appearance.append(appearance_image.subsurface((96, 0), (48, 48)))

        # 子弹爆炸特效
        boom_dynamic_image = pygame.image.load(r"image\special_effects\boom_dynamic.png").convert_alpha()
        self.boom = []
        self.boom.append(boom_dynamic_image.subsurface((0, 0), (48, 48)))
        self.boom.append(boom_dynamic_image.subsurface((48, 0), (48, 48)))
        self.boom.append(boom_dynamic_image.subsurface((96, 0), (48, 48)))
        self.boom.append(boom_dynamic_image.subsurface((144, 0), (48, 48)))
        self.boom.append(boom_dynamic_image.subsurface((192, 0), (48, 48)))
        self.boom.append(boom_dynamic_image.subsurface((240, 0), (48, 48)))

    # 显示保护罩的函数
    def SE_protect(self,screen,x,y,current):
        current = current % 2
        screen.blit(self.protect[current], (x, y))
    # 显示敌方出现的函数
    def SE_appearance(self,screen,x,y,current):
        if current <= 10:
            screen.blit(self.appearance[0], (x, y))
        elif current <= 20:
            screen.blit(self.appearance[1], (x, y))
        elif current <= 30:
            screen.blit(self.appearance[2], (x, y))
        elif current <= 40:
            screen.blit(self.appearance[0], (x, y))
        elif current <= 50:
            screen.blit(self.appearance[1], (x, y))
        elif current <= 60:
            screen.blit(self.appearance[2], (x, y))
        elif current <= 70:
            screen.blit(self.appearance[0], (x, y))
        elif current <= 80:
            screen.blit(self.appearance[1], (x, y))
        elif current <= 90:
            screen.blit(self.appearance[2], (x, y))
    # 显示爆炸的函数
    def SE_boom(self,screen,x,y,current):
        if current <= 5:
            screen.blit(self.boom[0],(x,y))
        elif current <= 10:
            screen.blit(self.boom[1],(x,y))
        elif current <= 15:
            screen.blit(self.boom[2],(x,y))
        elif current <= 20:
            screen.blit(self.boom[3],(x,y))
        elif current <= 25:
            screen.blit(self.boom[4],(x,y))
        elif current <= 30:
            screen.blit(self.boom[5],(x,y))
"""
子弹爆炸的记录位置的类
因为子弹爆炸需要特效，但子弹爆炸则子弹就消除了 但特效会维持 所以需要在子弹消失的时候记录下位置
"""
class bulletBoom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.times = 30
