import pygame
import random


class Recs(object): #função dos obstaculos (retangulos)
    def __init__(self, numeroinicial):
        self.lista = [] #array
        for x in range (numeroinicial): #vai pecorrer o for ate a posição do numero inicial
            leftrandom = random.randrange(2, 560)
            toprandom = random.randrange(-580, -10) #pra começar fora da tela
            width = random.randrange(10, 30)
            height = random.randrange(15, 30)
            self.lista.append(pygame.Rect(leftrandom, toprandom, width, height))

    def mover(self):
        for retangulo in self.lista:
            retangulo.move_ip(0, 2)

    def cor(self, superficie):
        for retangulo in self.lista:
            pygame.draw.rect(superficie, (165, 214, 254), retangulo)

    def recriar(self):
        for x in range (len(self.lista)):
            if self.lista[x].top > 481: #sempre que passar da tela, ele recria os obstaculos
                leftrandom = random.randrange(2, 560)
                toprandom = random.randrange(-580, -10) #pra começar fora da tela
                width = random.randrange(10, 30)
                height = random.randrange(15, 30)
                self.lista[x] = (pygame.Rect(leftrandom, toprandom, width, height)) #garantindo que so vai gerar um objeto e nao a lista toda
    
class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (100, 200) #posicao da imagem

    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie): #parametro de update
        superficie.blit(self.imagem, self.rect) #qnd chamar update ele mostra esses dois objetos


def colisao(player, recs): #criando colisão
    for rec in recs.lista: #rec é um dos retangulos da lista de retangulos
        if player.rect.colliderect(rec):
            return True

    return False
    

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
    imagem_explosao = pygame.image.load("imagens/explosao.png").convert_alpha()

    pygame.mixer.music.load("audios/musica.mp3")
    pygame.mixer.music.play(3)

    som_explosao = pygame.mixer.Sound("audios/explosao.wav")
    
    
    vx, vy = 0,0
    velocidade = 10
    leftpress, rightpress, uppress, downpress = False, False, False, False

    ret = Recs(30)
    colidiu = False

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if colidiu == False:

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

                        
        if colisao(jogador, ret):
            colidiu = True
            jogador.imagem = imagem_explosao
            pygame.mixer.music.stop()
            som_explosao.play()

        if colidiu == False:
            ret.mover()
            jogador.mover(vx, vy)
        

        relogio.tick(20)
        tela.blit(backg,(0,0))
        #ret.mover() #gerando obstaculos 
        ret.cor(tela) #pintando obstaculos
        ret.recriar() #chamando recriação dos obstaculos
        jogador.update(tela) #chamando o jogador na tela
        #jogador.mover(vx, vy)

        pygame.display.update()

    pygame.quit()

main()
