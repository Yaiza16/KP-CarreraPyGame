import pygame
import sys
import random

class Runner():
    __customes = ('turtle', 'fish', 'moray', 'octopus')
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("img/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
    
    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ("Speedy", "Lucera", "Alonso", "Torcuata")
    __startLine = -15
    __finishLine = 600
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #Aqui hemos cargado la imagen
        self.__background = pygame.image.load("img/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            corredor = Runner(self.__startLine, self.__posY[i])
            corredor.name = self.__names[i]
            self.runners.append(corredor)


    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(runner.name))
                    gameOver = True
            

            
            #Aqui llamamos a la imagen en las coordenadas
            self.__screen.blit(self.__background, (0, 0))
            
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)

                
            pygame.display.flip() #Actualiza la pantalla
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == '__main__':
    game = Game()
    pygame.init()
    game.competir()