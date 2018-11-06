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
    sup = pygame.Surface((600, 600))
    sup.fill(cor_azul)

    sup2 = pygame.Surface((100, 100))
    sup2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)
    ret2 = pygame.Rect(80, 100, 100, 60)

    
    sair = False

    pygame.font.init()
    
    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)
    texto = pygame.font.SysFont("Arial", 30, True, False)
    

    audio_explosao = pygame.mixer.Sound('AUDIOS.ogg')

    listaret = []

    for x in range(15):
        h = random.randrange(20, 90)
        w = random.randrange(15, 50)
        x = random.randrange(600)
        y = random.randrange(600)
        listaret.append(pygame.Rect(x, y, w, h))
        
    while sair != True: #Loop de while, cria uma variavel do tipo event que recebe um evento

        for rets in listaret:
            pygame.draw.rect(sup, cor_verde, rets)


        for event in pygame.event.get(): #ao clicar no X ele entra na condição IF
            if event.type == pygame.QUIT: #se o evento recebido for o QUIT, o sair passa a ser True
                sair = True #no momento que o sair passa a ser True, ele sai do while e executa o Quit
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ret.colliderect(ret2):
                    ret2.height = 0
                    ret2.width = 0

            #if event.type == pygame.MOUSEMOTION:
                #ret = ret.move(-10, -10)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ret.move_ip(-10, 0)  #utiliza move_ip para movimentar com teclado

                if event.key == pygame.K_RIGHT:
                    ret.move_ip(10, 0)

                if event.key == pygame.K_UP:
                    ret.move_ip(0, -10)

                if event.key == pygame.K_DOWN:
                    ret.move_ip(0, 10)

                if event.key == pygame.K_SPACE:
                    ret.move_ip(10, 10)

                if event.key == pygame.K_BACKSPACE:
                    ret.move_ip(-10, -10)
                

        relogio.tick(30) #tick pra atualizar
        tela.fill(cor_branca) #preencher o fundo da tela com cor branca
        tela.blit(sup, [0,0]) #chamando a superficie
        tela.blit(sup2, [250,50]) #chamando a superficie 2
        tela.blit(sup2, [250,150])
        
        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos() #Evento de captura do mouse
        ret.left -= ret.width/2   #Coloca cursos no centro do objeto ret
        ret.top -= ret.height/2
        '''if ret.colliderect(ret2): #testando colisão com objeto
            ret2.inflate_ip(3, 3)
            text = fonte_perdeu.render('COLIDIU', 1, (cor_vermelha)) #printando perdeu 
            audio_explosao.play()
            audio_explosao.set_volume(00.1)
            tela.blit(text, (150, 150))
            (ret.left, ret.top) = (xant, yant)'''

        segundos = pygame.time.get_ticks()/1000
        segundos = str(segundos)
        contador = texto.render(segundos, 0, cor_branca)
        tela.blit(contador, (300,10))
        
        pygame.draw.rect(tela, cor_vermelha, ret) #inserindo retangulo
        pygame.draw.rect(tela, cor_rosa, ret2)
        pygame.display.update() #Chamar atualização na Tela
        
    pygame.quit() #Quita o game ao clicar no X
        
        

main()
