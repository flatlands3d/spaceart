import socket
import nmcli

def testConnection():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout = 3)
        return True
    except OSError:
        return False

def startHotspot():
    try:
        nmcli.device.wifi_hotspot(
            ifname = "wlan0",
            con_name = "Countdown Clock Config Hotspot",
            ssid = "Countdown Clock",
            password = "SecurePassword123"
        )
    except Exception as e:
        print(e)

def disconnectNetworks():
    activeConnections = nmcli.connection.show_all(active = True)
    for conn in activeConnections:
        if getattr(conn, 'type', '') == 'wifi':
            nmcli.connection.down(conn)

def changeNetwork():
    print("Change Requested")
    disconnectNetworks()
    startHotspot()