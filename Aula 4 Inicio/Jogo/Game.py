import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (100, 200)

    def mover(self, vx, vy):
        pass


    def update(self, superficie):
        pass
