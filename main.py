import pygame

class Game():
    corredores = []
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("img/background.png")
    
    def competir(self):
        while True:
            #comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
if __name__ == '__main__':
    pygame.init()
    game = Game()
    