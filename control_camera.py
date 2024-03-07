# import serial
# import serial.rs485
import requests
import time

# https://community.ptzoptics.com/s/article/How-do-I-get-the-PTZOptics-camera-up-on-my-network-Quick-Setup

#https://ptzoptics.com/networking-help-setting-up-a-ptz-camera-on-your-network/

# Note: made network IP 192.168.100.90, gateway 192.168.100.1, netmask 255.255.255.0
# Camera IP is 192.168.100.88



def sendCameraControl(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print("Command: " + url + " was successful")
        return "success"
    else:
        print("An Error occured while ")
        return "success"

# buildUrl will create the HTTP CGI commands using the data passed to it.
# Once finished it will return the processed url to the function that called it.
def buildCgiUrl(command):
    url = 'http://' + "192.168.100.88" + '/cgi-bin/ptzctrl.cgi?ptzcmd&'
    action = command #"up" #req["param[action]"]
    panSpeed = str(24)
    tiltSpeed = str(20)

    # All vector motion actions
    if action == "up" or action == "down" or action == "left" or action =="right":
        # panSpeed = req["param[panSpeed]"]
        # tiltSpeed = req["param[tiltSpeed]"]
        return url + action + '&' + panSpeed + '&' + tiltSpeed
    # All non-directional motion actions
    elif action == "home" or action == "ptzstop":
        return url + action
    # All Focus actions
    elif action == "focusin" or action == "focusout" or action == 'focusstop':
        focusSpeed = req["param[focusSpeed]"]
        return url + action + '&' + focusSpeed
    # All Zoom actions
    elif action == "zoomin" or action == "zoomout" or action == 'zoomstop':
        zoomSpeed = req["param[zoomSpeed]"]
        return url + action + '&' + zoomSpeed
    else:
        return url + 'home' + '&10&10';

# pan speed goes up to 24
# tilt speed goes up to 20

def post(command):
    return sendCameraControl(buildCgiUrl(command))

# post("up")
# time.sleep(1)
# post("down")
# time.sleep(1)
# post("ptzstop")

# post("home")
# time.sleep(2)
# post("left")
# time.sleep(1)
# post("ptzstop")
