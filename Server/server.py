from flask import Flask, request
from Server.ONVIFCameraControl import ONVIFCameraControl as OCC

app = Flask(__name__)
cam = OCC(("172.18.200.56", 80), "admin", "Supervisor", "wsdl")

@app.route('/continuous_move', methods=['POST'])
def move_continuous():
    data = request.json
    cam.move_continuous(data['ptz'])
    return 'ok'

@app.route('/go_home', methods=['POST'])
def go_home():
    cam.go_home()
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True, port=5000)