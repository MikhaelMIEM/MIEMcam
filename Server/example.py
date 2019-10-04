from Server.ONVIFCameraControl import ONVIFCameraControl as OCC
from time import sleep

if __name__ == '__main__':
    cam = OCC(("172.18.200.55", 80), "admin", "Supervisor", "wsdl")
    #cam = OCC(("192.168.15.42", 80), "admin", "Supervisor", "wsdl")
    #cam = OCC(("172.18.199.41", 8899), "admin", "Supervisor", "wsdl")

    cam.move_continuous((1, 1, 1))
    sleep(1)
    cam.set_preset(1)
    cam.move_continuous((-1, -1, -1))
    sleep(1)
    cam.stop()
    cam.set_preset(2)
    sleep(1)
    cam.goto_preset(1)
    sleep(2)
    cam.goto_preset(2)
    sleep(2)
    cam.go_home()
    print(cam.get_presets()[0])

    cam.set_brightness(0)
    sleep(1)
    cam.set_brightness(100)
    sleep(1)
    cam.set_brightness(50)

    cam.move_focus_continuous(1)
    sleep(4)
    cam.stop_focus()
    cam.move_focus_continuous(-1)
    sleep(4)
    cam.stop_focus()
    cam.move_focus_absolute(0.9, 0.1)
    cam.set_focus_mode('AUTO')
    print(cam.get_stream_uri(protocol='RTSP', stream='RTP-Multicast'))
