from ONVIFCameraControl import ONVIFCameraControl as OCC
from RtspProxiesPool import RtspProxiesPool
from time import sleep
import keyboard
import cv2

cams = [
    {
        "addr":
            {
                "ip": "172.18.200.52",
                "port": 80
            },
        "user": "admin",
        "password": "Supervisor",
        "room": "504",
        "uid": "fawuifq",
        "name": "214"
    },
    {
        "addr":
            {
                "ip": "172.18.200.53",
                "port": 80
            },
        "user": "admin",
        "password": "Supervisor",
        "room": "504",
        "uid": "fawuifq1",
        "name": "2134"
    },
]

if __name__ == '__main__':

    rtspProxiesPool = RtspProxiesPool()

    for cam in cams:
        rtspProxiesPool.add_proxy(cam)
        uid = cam['uid']
        port = rtspProxiesPool.get_port(uid)  # More information at this function docstring

    print('Press enter to end proxying')
    input()

    # to watch stream type in command line 'vlc rtsp://camera_ip'
    # cam = OCC(("172.18.200.53", 80), "admin", "Supervisor", "wsdl")
    # cam = OCC(("192.168.15.42", 80), "admin", "Supervisor", "wsdl")
    # cam = OCC(("172.18.199.41", 8899), "admin", "Supervisor", "wsdl")

    # while True:
    #     key = keyboard.read_key()
    #     if key == 'j':
    #         print("down")
    #         cam.move_continuous((0, -1, 0))
    #         sleep(1)
    #         cam.stop()
    #
    #     if key == "k":
    #         print("up")
    #         cam.move_continuous((0, 1, 0))
    #         sleep(1)
    #         cam.stop()
    #
    #     if key == "l":
    #         print("right")
    #         cam.move_continuous((1, 0, 0))
    #         sleep(1)
    #         cam.stop()
    #
    #     if key == "h":
    #         print("left")
    #         cam.move_continuous((-1, 0, 0))
    #         sleep(1)
    #         cam.stop()
