import pygame
from pygame.locals import * #Para el keydown, key up
import sys
import random

class Runner():
    __customes = ('turtle', 'fish', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("img/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""


class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #Aqui hemos cargado la imagen
        self.__background = pygame.image.load("img/background.png")
        pygame.display.set_caption("Carrera de bichos")
    
        self.runner = Runner(320, 240)
    
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        runnerY = self.runner.position[1]
                        runnerY += -5 #Porque la parte superior izquierda de la pantalla es la coordenada (0,0) en pygame
                        self.runner.position[1] = runnerY   
                    elif event.key == K_DOWN:
                        runnerY = self.runner.position[1]
                        runnerY += 5
                        self.runner.position[1] = runnerY
                    elif event.key == K_LEFT:
                        runnerY = self.runner.position[0]
                        runnerY += -5
                        self.runner.position[0] = runnerY
                    elif event.key == K_RIGHT:
                        runnerY = self.runner.position[0]
                        runnerY += 5
                        self.runner.position[0] = runnerY
                    else:
                        pass
        
            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
            
if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.start()

            
