import pygame

def main(): #parametros de Display
    #As definições dos objetos(variaveis)
    pygame.init() #Inicializando o pygame
    tela = pygame.display.set_mode([600, 450]) #Setando a dimensao da tela
    pygame.display.set_caption("Jogo Iniciante") #Exibindo titulo do game
    relogio = pygame.time.Clock()
    cor_branca = (255,255,255)
    cor_azul = (108,194,236) #variaveis de corer, # RGB
    cor_verde = (54,182,112)
    cor_vermelha = (227,57,9)
    cor_rosa = (253, 147, 226)
    sup = pygame.Surface((600, 450))
    sup.fill(cor_azul)
    
    ret = pygame.Rect(10, 10, 30, 30)
    ret2 = pygame.Rect(10, 40, 555, 6)
    sair = False

    pygame.font.init()
    
    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

    audio_explosao = pygame.mixer.Sound('AUDIOS.ogg')
        
    while sair != True: #Loop de while, cria uma variavel do tipo event que recebe um evento
        for event in pygame.event.get(): #ao clicar no X ele entra na condição IF
            if event.type == pygame.QUIT: #se o evento recebido for o QUIT, o sair passa a ser True
                sair = True #no momento que o sair passa a ser True, ele sai do while e executa o Quit
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(150, 150) #Movimenta o retangulo ao clicar                

        relogio.tick(30) #tick pra atualizar
        tela.fill(cor_branca) #preencher o fundo da tela com cor branca
        tela.blit(sup, [0,0]) #chamando a superficie
        
        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos() #Evento de captura do mouse
        ret.left -= ret.width/2   #Coloca cursos no centro do objeto ret
        ret.top -= ret.height/2
        if ret.colliderect(ret2): #testando colisão com objeto
            text = fonte_perdeu.render('COLIDIU', 1, (cor_vermelha)) #printando perdeu 
            tela.blit(text, (150, 150))
            audio_explosao.play()
            audio_explosao.set_volume(00.1)
            (ret.left, ret.top) = (xant, yant)

        if ret.top > 400:
            text = fonte_perdeu.render('VOCE GANHOU', 1, (cor_branca)) #printando perdeu 
            tela.blit(text, (200, 200))
            ret2.left = 602

            
        pygame.draw.rect(tela, cor_vermelha, ret) #inserindo retangulo
        pygame.draw.rect(tela, cor_rosa, ret2)
        pygame.display.update() #Chamar atualização na Tela
        
    pygame.quit() #Quita o game ao clicar no X
        
        

main()
