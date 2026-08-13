import pygame

class Overlay:
    cycle = True
    screen = pygame.display.set_mode((480, 720))
    background = pygame.image.load("images/load.png").convert()
    background = pygame.transform.scale(background, (480, 720))

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Space Art")
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def updateBackground(self, image):
        self.background = pygame.image.load("images/f9.jpg").convert()
        self.background = pygame.transform.scale(self.background, (480, 720))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def updateTimer(self, countDown):
        font = pygame.font.Font("7segment.ttf", 50)
        blank = font.render("00:00:00", True, (172, 172, 172))
        self.screen.blit(blank, (50, 150))
        timer = font.render(countDown, True, (255, 255, 255))
        self.screen.blit(timer, (50, 150))
        font = pygame.font.SysFont("Arial", 10)
        days = font.render("DAYS", True, (255, 255, 255))
        self.screen.blit(days, (60, 200))
        hours = font.render("HOURS", True, (255, 255, 255))
        self.screen.blit(hours, (111, 200))
        minutes = font.render("MINUTES", True, (255, 255, 255))
        self.screen.blit(minutes, (161, 200))
        pygame.display.flip()

    def updateTitleBlock(self, lsp, vehicle, mission, location):
        font = pygame.font.SysFont("Arial", 10)
        line1 = font.render(lsp, True, (255, 255, 255))
        self.screen.blit(line1, (300, 150))
        line2 = font.render(vehicle, True, (255, 255, 255))
        self.screen.blit(line2, (300, 175))
        line3 = font.render(mission, True, (255, 255, 255))
        self.screen.blit(line3, (300, 200))
        line4 = font.render(location, True, (255, 255, 255))
        self.screen.blit(line4, (300, 225))
        pygame.display.flip()