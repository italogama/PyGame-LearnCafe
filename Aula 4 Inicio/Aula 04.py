import pygame

def main(): #parametros de Display
    pygame.init() #Inicializando o pygame
    pygame.display.set_mode([300, 300]) #Setando a dimensao da tela
    pygame.display.set_caption("Iniciando com PyGame") #Exibindo titulo do game
    
    sair = False

    while sair != True: #Loop de while, cria uma variavel do tipo event que recebe um evento
        for event in pygame.event.get(): #ao clicar no X ele entra na condição IF
            if event.type == pygame.QUIT: #se o evento recebido for o QUIT, o sair passa a ser True
                sair = True #no momento que o sair passa a ser True, ele sai do while e executa o Quit

    
    pygame.display.update() #Chamar atualização na Tela
    pygame.quit() #Quita o game ao clicar no X
        
        

main()
