# Space Art v0.1
# Flatlands3D - Ethan Doerksen
# 08/06/26

import pygame
import sys
from launch import Launch
from overlay import Overlay

imageDict = { # This dictionary links the launch library vehicle name to a background image
    "Ariane 62" : "images/a62.jpg",
    "Electron" : "images/electron.jpg",
    "Falcon 9 Block 5" : "images/f9.jpg",
    "Falcon Heavy" : "images/fh.jpg",
    "Firefly Alpha Block 2" : "images/alpha2",
    "Starship" : "images/ss.jpg",
    "Vulcan VC6L" : "images/vc6l.jpg"
}

o1 = Overlay()
l1 = Launch()
cycle = True
clock = pygame.time.Clock()
refresh = pygame.USEREVENT + 1
pygame.time.set_timer(refresh, 60000) # Sets the update frequency, currently set to 60 seconds

if __name__ == "__main__":
    startEvent = pygame.event.Event(refresh) # Post refresh event when main loop starts
    pygame.event.post(startEvent) # Otherwise the screen will be black for the refresh period
    while cycle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cycle = False
            elif event.type == refresh:
                l1.updateLaunch()
                totalSeconds = l1.deltaTime.total_seconds()
                days, remainder = divmod(totalSeconds, 86400)
                hours, remainder = divmod(remainder, 3600)
                minutes, seconds = divmod(remainder, 60)
                tMinus = f"{int(days):02}:{int(hours):02}:{int(minutes):02}"
                o1.updateBackground(imageDict.get(l1.vehicle))
                o1.updateTitleBlock(l1.lsp, l1.vehicle, l1.mission, l1.pad)
                o1.updateTimer(tMinus)
        clock.tick(30)
    pygame.quit()
    sys.exit()