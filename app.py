from flask import Flask, render_template
from motors import update_state

app = Flask(__name__)


def render_main():
    return render_template('main.html')


@app.route("/<state>")
def update_robot(state=None):
    update_state(state)
    return "ok"


@app.route("/")
def root():
    return render_main()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
