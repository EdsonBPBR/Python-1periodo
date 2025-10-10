import pygame

pygame.init()

dimensoes_tela = (600, 600)
screnn = pygame.display.set_mode(dimensoes_tela)
pygame.display.set_caption("Campo de Batalha 1940")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            pass