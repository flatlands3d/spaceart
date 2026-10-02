from flask import Flask, render_template, redirect, request
import time
import nmcli
import networking

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"]) # Default route
def captivePortal():
    message = None
    networkList = nmcli.device.wifi()
    ssidList = set(net.ssid for net in networkList if net.ssid and net.ssid != "Countdown Clock")
    if request.method == "POST":
        message = "Attempting to Connect to Network"
        time.sleep(5)
        try:
            # nmcli.connection.down("Countdown Clock")
            nmcli.device.wifi_connect(request.form.get("wifi_ssid"), request.form.get("wifi_password"))
        except Exception as e:
            message = "Invalid Password"
            print(e)
            networking.startHotspot()
            time.sleep(2)
    return render_template("network_login.html", networks = ssidList, status = message)

@app.route("/hotspot-detect.html") # Apple captive route
def appleProbe():
    return redirect('/', code = 302)