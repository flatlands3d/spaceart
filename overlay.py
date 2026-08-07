import pygame

class Overlay:
    cycle = True
    screen = pygame.display.set_mode((480, 720))

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Art")

    def updateBackground(self, image):
        background = pygame.image.load("images/f9.jpg")
        background = pygame.transform.scale(background, (480, 720))
        self.screen.blit(background, (0, 0))
        pygame.display.flip()

    def updateTimer(self, countDown):
        font = pygame.font.SysFont("Arial", 40)
        timer = font.render(countDown, True, (255, 255, 255))
        self.screen.blit(timer, (100, 150))
        pygame.display.flip()