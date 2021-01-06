import pygame
import sys

class Game():
    runners = []
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #Aqui hemos cargado la imagen
        self.__background = pygame.image.load("img/background.png")
        pygame.display.set_caption("Carrera de bichos")

    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            #Aqui llamamos a la imagen en las coordenadas
            self.__screen.blit(self.__background, (0, 0))
            pygame.display.flip() #Actualiza la pantalla
        
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()