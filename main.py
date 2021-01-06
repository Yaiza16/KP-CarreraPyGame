import pygame
import sys

class Runner():

class Game():
    corredores = []
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("img/background.png")
        
        self.runner = pygame.image.load("img/fish.png")
    
    def competir(self):
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
            #comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #pygame.QUIT es darle a la cruz de la pantalla que se abre, por tanto, se cerraría.
                    pygame.quit()
                    sys.exit()
             
            #Refrescar / renderizar la pantalla 
            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip() #Actualiza la pantalla
            
            x += 3
            if x >=250:
                hayGanador = True
            
        pygame.quit()
        sys.exit()
    
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    