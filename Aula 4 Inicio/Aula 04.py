import pygame

def main(): #parametros de Display
    #As definições dos objetos(variaveis)
    pygame.init() #Inicializando o pygame
    tela = pygame.display.set_mode([300, 300]) #Setando a dimensao da tela
    pygame.display.set_caption("Iniciando com PyGame") #Exibindo titulo do game
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_azul = (108,194,236) #variaveius de corer, # RGB
    cor_verde = (54,182,112)
    cor_vermelha = (227,57,9)
    sup = pygame.Surface((200, 200))
    sup.fill(cor_azul)

    sup2 = pygame.Surface((100, 100))
    sup2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)

    
    sair = False

    while sair != True: #Loop de while, cria uma variavel do tipo event que recebe um evento
        for event in pygame.event.get(): #ao clicar no X ele entra na condição IF
            if event.type == pygame.QUIT: #se o evento recebido for o QUIT, o sair passa a ser True
                sair = True #no momento que o sair passa a ser True, ele sai do while e executa o Quit
                
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #ret = ret.move(10, 10) #Movimenta o retangulo ao clicar

            #if event.type == pygame.MOUSEMOTION:
                #ret = ret.move(-10, -10)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ret.move(-10, 0)
                

        relogio.tick(27) #tick pra atualizar
        tela.fill(cor_branca) #preencher o fundo da tela com cor branca
        tela.blit(sup, [50,50]) #chamando a superficie
        tela.blit(sup2, [250,50]) #chamando a superficie 2
        tela.blit(sup2, [250,150])
        pygame.draw.rect(tela, cor_vermelha, ret) #inserindo retangulo
        pygame.display.update() #Chamar atualização na Tela
        
    pygame.quit() #Quita o game ao clicar no X
        
        

main()
