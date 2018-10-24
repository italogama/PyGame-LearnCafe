import pygame
import random

def main():
    #As definições dos objetos(variaveis)
    pygame.init()
    tela = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Iniciando com Pygame")
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_azul = (108,194,236)
    cor_verde = (54,182,112)
    cor_vermelha = (227,57,9)
    cor_rosa = (253,147,226)
    sair = False 

    imagem = pygame.image.load("imagens/nave.png")
    (x,y) = (150, 150)
    vx = 0
    vy = 0

    ret = pygame.Rect(250, 300, 20, 500)

    sprite = pygame.sprite.Sprite()
    sprite.image = imagem
    sprite.rect = imagem.get_rect()
    sprite.rect.top = 50
    sprite.rect.left = 50

    while sair != True:

                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
                
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
                
                

        if sprite.rect.colliderect(ret):
            sprite.rect.left = oldx
            sprite.rect.top = oldy
            
        x += vx
        y += vy
        relogio.tick(100)
        tela.fill(cor_branca)
        #tela.blit(imagem, (x,y))

        #(x,y) = pygame.mouse.get_pos()
        pygame.draw.rect(tela, cor_vermelha, ret)

        oldx = sprite.rect.left
        oldy = sprite.rect.top
        tela.blit(sprite.image, sprite.rect)
        sprite.rect.move_ip(vx, vy)
        
        pygame.display.update()
        
    pygame.quit()       


main()
