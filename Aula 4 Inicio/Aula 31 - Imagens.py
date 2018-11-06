import pygame
import random

def main(): #parametros de Display
    #As definições dos objetos(variaveis)
    pygame.init() #Inicializando o pygame
    tela = pygame.display.set_mode([600, 600]) #Setando a dimensao da tela
    pygame.display.set_caption("Iniciando com PyGame") #Exibindo titulo do game
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_azul = (108,194,236) #variaveis de corer, # RGB
    cor_verde = (54,182,112)
    cor_vermelha = (227,57,9)
    cor_rosa = (253, 147, 226)
    sair = False

    imagem = pygame.image.load("imagens/nave.png") #inserindo imagem
    (x,y) = (150,150)
    vx = 0
    vy = 0

    ret = pygame.Rect(250, 300, 20, 500)

    sprit = pygame.sprite.Sprit()
    sprite.image = imagem
    sprit.rect = imagem.get_rect()
    sprit.rect.top = 50
    sprit.rect.left = 50
        
    while sair != True: #Loop de while, cria uma variavel do tipo event que recebe um evento

        for event in pygame.event.get(): #ao clicar no X ele entra na condição IF
            if event.type == pygame.QUIT: #se o evento recebido for o QUIT, o sair passa a ser True
                sair = True #no momento que o sair passa a ser True, ele sai do while e executa o Quit
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vx -= 5

                if event.key == pygame.K_RIGHT:
                    vx += 5

                if event.key == pygame.K_DOWN:
                    vy += 5

                if event.key == pygame.K_UP:
                    vy -= 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    vx = 0

                if event.key == pygame.K_RIGHT:
                    vx = 0

                if event.key == pygame.K_DOWN:
                    vy = 0

                if event.key == pygame.K_UP:
                    vy = 0

            x += vx
            y += vy
            relogio.tick(100)
            tela.fill(cor_branca)
            tela.blit(imagem, (x,y))

            #(x,y) = pygame.mouse.get_pos()
            pygame.draw.rect(tela, cor_vermelha, ret)
            
            pygame.display.update() #Chamar atualização na Tela
        
    pygame.quit() #Quita o game ao clicar no X
        
        

main()
