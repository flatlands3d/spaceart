import requests
import datetime

class Launch:
    api = "https://lldev.thespacedevs.com/2.3.0/launches/upcoming/"
    lsp = "" # Launch service provider
    vehicle = "" # Launch vehicle
    mission = "" # Mission name
    pad = "" # Launch site
    launchDate = datetime.datetime(1, 1, 1, 0, 0, 0, tzinfo = datetime.UTC) # Date and time of launch in UTC
    deltaTime = datetime.datetime(1, 1, 1, 0, 0, 0, tzinfo = datetime.UTC) # Time until launch

    def __init__(self):
        pass

    def updateLaunch(self):
        response = requests.get(self.api, params = {"limit": 4})
        if response.status_code == 200:
            data = response.json()
            for launch in data.get("results", []):
                title = launch.get("name").split(" | ")
                self.vehicle = title[0]
                self.mission = title[1]
                self.pad = (launch.get("pad", {})).get("name")
                self.lsp = (launch.get("launch_service_provider", {})).get("name")
                self.launchDate = datetime.datetime.fromisoformat(launch.get("window_start"))
                self.deltaTime = self.launchDate - datetime.datetime.now(datetime.timezone.utc)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")