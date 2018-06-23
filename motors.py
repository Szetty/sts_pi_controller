def init_eh():
    try:
        return __import__("explorerhat")
    except ImportError:
        print("Explorer Hat module is not present")
        return None


eh = init_eh()


def forward():
    eh.motor.one.backwards(100)
    eh.motor.two.forwards(100)


def backward():
    eh.motor.one.forwards(100)
    eh.motor.two.backwards(100)


def left():
    eh.motor.two.stop()
    eh.motor.one.backwards(100)


def right():
    eh.motor.one.stop()
    eh.motor.two.forwards(100)


def stop():
    eh.motor.one.stop()
    eh.motor.two.stop()


def clockwise():
    eh.motor.one.forwards(100)
    eh.motor.two.forwards(100)


def anti_clockwise():
    eh.motor.one.backwards(100)
    eh.motor.two.backwards(100)


stateToFunction = {
    "forward": forward,
    "back": backward,
    "left": left,
    "right": right,
    "stop": stop,
    "clockwise": clockwise,
    "anti-clockwise": anti_clockwise
}


def update_state(state):
    try:
        f = stateToFunction[state]
        if eh is None:
            print("State #" + f.__name__ + "# was called")
        else:
            f()
    except KeyError:
        print("No state with name " + state)
