import pygame
"""
修改时间：2021.12.15
修改人：2019051604048 詹孝东
模块描述：
该模块是墙体类，继承了pygame的精灵类，主要就是使用image显示图片 用rect改变位置
最后是用地图类保存这些
详细情况情况下方代码
"""
# 该模块是地图元素类基础元素类 包含砖块类、石头类、河流类、树类、冰类和基地类

# 将图片加载
brickImage = r"image\wall\brick.png"
ironImage = r"image\wall\iron.png"
riverImage = r"image\wall\river1.png"
treeImage = r"image\wall\tree.png"
iceImage = r"image\wall\ice.png"
# 基地的图片
homeImage = r"image\home.png"
# 这些类继承pygame的精灵类 精灵可以认为成是一个个小图片，一种可以在屏幕上移动的图形对象，并且可以与其他图形对象交互
#砖块的类
class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #加载图片
        self.image = pygame.image.load(brickImage)
        #get_rect()是一个处理矩形图像的方法
        self.rect = self.image.get_rect()

#石头的类
class Iron(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(ironImage)
        self.rect = self.image.get_rect()
# 河流类
class River(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(riverImage)
        self.rect = self.image.get_rect()

# 树类
class Tree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(treeImage)
        self.rect = self.image.get_rect()

# 冰地板类
class Ice(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(iceImage)
        self.rect = self.image.get_rect()

# 家的类
class Home(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # 加载图片
        self.image = pygame.image.load(homeImage)
        # get_rect()是一个处理矩形图像的方法
        self.rect = self.image.get_rect()