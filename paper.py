from inky.auto import auto
from PIL import ImageFont, Image, ImageDraw

class PaperScreen:
    display = auto()
    timerFont = ImageFont.truetype("fonts/7segment.ttf", 100)
    infoFont = ImageFont.load_default(20)

    clockLocDict = {
        "Ariane 62" : (600, 120), # Done
        "Electron" : (600, 120), # Done
        "Falcon 9 Block 5" : (600, 120), # Done
        "Falcon Heavy" : (600, 120), # Done
        "Firefly Alpha Block 2" : (600, 120),
        "Starship" : (600, 120),
        "Vulcan VC6L" : (900, 150)
    }

    infoLocDict = {
        "Ariane 62" : (25, 1475), # Done
        "Electron" : (25, 1475), # Done
        "Falcon 9 Block 5" : (25, 1475), # Done
        "Falcon Heavy" : (25, 1475), # Done
        "Firefly Alpha Block 2" : (25, 1475),
        "Starship" : (25, 1475),
        "Vulcan VC6L" : (25, 1475) # Done
    }

    def __init__(self):
        pass

    def initializeScreen(self):
        self.display = auto()

    def createImage(self, image, time, lsp, vehicle, mission, pad):
        img = Image.open(image)
        draw = ImageDraw.Draw(img)
        # Countdown block
        draw.text(self.clockLocDict.get(vehicle), "88:88:88", font = self.timerFont, fill = "grey", anchor = "mm")
        draw.text(self.clockLocDict.get(vehicle), time, font = self.timerFont, fill = "white", anchor = "mm")
        draw.text(tuple(x + y for x, y in zip(self.clockLocDict.get(vehicle), (-110, 60))), "DAYS", font = self.infoFont, fill = "white", anchor = "mm")
        draw.text(tuple(x + y for x, y in zip(self.clockLocDict.get(vehicle), (0, 60))), "HOURS", font = self.infoFont, fill = "white", anchor = "mm")
        draw.text(tuple(x + y for x, y in zip(self.clockLocDict.get(vehicle), (112, 60))), "MINUTES", font = self.infoFont, fill = "white", anchor = "mm")
        # Title block
        draw.text(self.infoLocDict.get(vehicle), lsp, font = self.infoFont, fill = "white")
        draw.text(tuple(x + y for x, y in zip(self.infoLocDict.get(vehicle), (0, 25))), vehicle, font = self.infoFont, fill = "white")
        draw.text(tuple(x + y for x, y in zip(self.infoLocDict.get(vehicle), (0, 50))), mission, font = self.infoFont, fill = "white")
        draw.text(tuple(x + y for x, y in zip(self.infoLocDict.get(vehicle), (0, 75))), pad, font = self.infoFont, fill = "white")
        img = img.transpose(Image.Transpose.ROTATE_270)
        self.display.set_image(img, saturation = 0.5)
        self.display.show()