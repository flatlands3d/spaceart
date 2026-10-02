# Space Art v1.0
# Flatlands3D - Ethan Doerksen
# 10/02/26

from launch import Launch
from paper import PaperScreen
from gpiozero import Button
import time
import threading
import webserver
import subprocess
import networking

imageDict = { # This dictionary links the launch library vehicle name to a background image
    "Ariane 62" : "/home/ofhserver/spaceart/spaceart/images/a62.jpg",
    "Electron" : "/home/ofhserver/spaceart/spaceart/images/electron.jpg",
    "Falcon 9 Block 5" : "/home/ofhserver/spaceart/spaceart/images/f9.jpg",
    "Falcon Heavy" : "/home/ofhserver/spaceart/spaceart/images/fh.jpg",
    "Firefly Alpha Block 2" : "/home/ofhserver/spaceart/spaceart/images/alpha2.jpg",
    "Starship" : "/home/ofhserver/spaceart/spaceart/images/ss.jpg",
    "Vulcan VC6L" : "/home/ofhserver/spaceart/spaceart/images/vc6l.jpg",
    "No Connection" : "/home/ofhserver/spaceart/spaceart/images/wifi.jpg"
}

buttonA = Button(5)
buttonB = Button(6)
buttonC = Button(25)
buttonD = Button(24)

buttonD.when_activated = networking.changeNetwork

l1 = Launch()
p1 = PaperScreen()
webserverThread = threading.Thread(target = webserver.app.run, args = ("0.0.0.0", 80))

if __name__ == "__main__":
    print("Welcome to Space Art v1.0 by Flatlands3D")
    p1.initializeScreen()
    if not networking.testConnection():
        print("No Wi-fi Connection.")
        p1.displayImage(imageDict.get("No Connection"))
        networking.startHotspot()
        time.sleep(2)
        webserverThread.start()
        while True:
            if networking.testConnection():
                break
            time.sleep(5)
    print("Connection Successful!")
    print("Checking for Updates...")
    subprocess.run("sudo apt update", shell = True, check = True)
    subprocess.run("sudo apt upgrade -y", shell = True, check = True)
    print("Done!")
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