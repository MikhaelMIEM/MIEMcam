from RtspProxiesPool import RtspProxiesPool

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