from flask import Flask, render_template, Response
from motors import update_state
from camera.camera import get_frame

app = Flask(__name__)


def render_main():
    return render_template('main.html')


@app.route("/<state>")
def update_robot(state=None):
    update_state(state)
    return "ok"


@app.route('/video')
def video():
    frame = get_frame()
    response = (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(response, mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def root():
    return render_main()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
