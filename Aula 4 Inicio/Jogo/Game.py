import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (200, 200) #posicao da imagem

    def mover(self, vx, vy):
        pass

    def update(self, superficie): #parametro de update
        superficie.blit(self.imagem, self.rect) #qnd chamar update ele mostra esses dois objetos

def main():
    import pygame
    pygame.init()
    tela = pygame.display.set_mode((480, 300)) #tamanho da area que vai utilizar
    sair = False
    relogio = pygame.time.Clock()

    img_nave = pygame.image.load("../imagens/nave.png").convert_alpha()
    jogador = Player(img_nave)

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

        relogio.tick(20)
        tela.fill((200, 200, 200))
        jogador.update(tela)

        pygame.display.update()


    pygame.quit()

main()
