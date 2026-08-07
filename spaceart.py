# Space Art v0.1
# Flatlands3D - Ethan Doerksen
# 08/06/26

import pygame
import sys
from launch import Launch
from overlay import Overlay

imageDict = {
    "Falcon 9 Block 5" : "images/f9.jpg",
    "Starship" : "images/ss.jpg"
}

o1 = Overlay()
l1 = Launch()
cycle = True
clock = pygame.time.Clock()
refresh = pygame.USEREVENT + 1
pygame.time.set_timer(refresh, 60000)

if __name__ == "__main__":
    while cycle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cycle = False
            elif event.type == refresh:
                l1.updateLaunch()
                print(l1.mission)
                print(l1.lsp)
                print(l1.vehicle)
                print(l1.deltaTime)
                print(l1.pad)
                totalSeconds = l1.deltaTime.total_seconds()
                days, remainder = divmod(totalSeconds, 86400)
                hours, remainder = divmod(remainder, 3600)
                minutes, seconds = divmod(remainder, 60)
                tMinus = f"{int(days)}:{int(hours)}:{int(minutes)}"
                o1.updateBackground(imageDict.get(l1.vehicle))
                o1.updateTimer(tMinus)
        clock.tick(30)
    pygame.quit()
    sys.exit()