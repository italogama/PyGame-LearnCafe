import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (100, 200) #posicao da imagem

    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie): #parametro de update
        superficie.blit(self.imagem, self.rect) #qnd chamar update ele mostra esses dois objetos

def main():
    import pygame
    #declaração das variaveis (objetos)
    pygame.init()
    tela = pygame.display.set_mode((480, 300)) #tamanho da area que vai utilizar
    sair = False
    relogio = pygame.time.Clock()

    img_nave = pygame.image.load("imagens/nave.png").convert_alpha()
    jogador = Player(img_nave)

    backg = pygame.image.load("imagens/fundo.png").convert_alpha()
    
    vx, vy = 0,0
    velocidade = 10
    leftpress, rightpress, uppress, downpress = False, False, False, False

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.KEYDOWN: #evento de tecla pressionada
                if event.key == pygame.K_LEFT:
                    leftpress = True
                    vx = - velocidade

                if event.key == pygame.K_RIGHT:
                    rightpress = True
                    vx = velocidade

                if event.key == pygame.K_UP:
                    uppress = True
                    vy = - velocidade

                if event.key == pygame.K_DOWN:
                    downpress = True
                    vy = velocidade

            if event.type == pygame.KEYUP: #evento de tecla não pressionada
                if event.key == pygame.K_LEFT:
                    leftpress = False
                    if rightpress:vx = velocidade
                    else:vx = 0

                if event.key == pygame.K_RIGHT:
                    rightpress = False
                    if leftpress:vx = -velocidade
                    else:vx = 0

                if event.key == pygame.K_UP:
                    uppress = False
                    if downpress:vx = velocidade
                    vy = 0

                if event.key == pygame.K_DOWN:
                    downpress = False
                    if uppress:vx = -velocidade
                    vy = 0


        relogio.tick(20)
        tela.blit(imagem_backg,(0,0))
        jogador.update(tela) #chamando o jogador na tela
        jogador.mover(vx, vy)

        pygame.display.update()

    pygame.quit()

main()
