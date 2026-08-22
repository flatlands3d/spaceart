# Space Art v0.2
# Flatlands3D - Ethan Doerksen
# 08/22/26

from launch import Launch
from paper import PaperScreen
import time

imageDict = { # This dictionary links the launch library vehicle name to a background image
    "Ariane 62" : "images/a62.jpg",
    "Electron" : "images/electron.jpg",
    "Falcon 9 Block 5" : "images/f9.jpg",
    "Falcon Heavy" : "images/fh.jpg",
    "Firefly Alpha Block 2" : "images/alpha2.jpg",
    "Starship" : "images/ss.jpg",
    "Vulcan VC6L" : "images/vc6l.jpg"
}

l1 = Launch()
p1 = PaperScreen()

if __name__ == "__main__":
    p1.initializeScreen()
    while True:
        status = l1.updateLaunch(imageDict)
        if status == 0:
            totalSeconds = l1.deltaTime.total_seconds()
            days, remainder = divmod(totalSeconds, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)
            tMinus = f"{int(days):02}:{int(hours):02}:{int(minutes):02}"
            p1.createImage(imageDict.get(l1.vehicle), tMinus, l1.lsp, l1.vehicle, l1.mission, l1.pad)
        elif status == 1:
            print("Error retriving data from Launch Library")
        elif status == 2:
            print("Error connecting to the internet")
        time.sleep(300)