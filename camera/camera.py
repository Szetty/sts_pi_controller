def init_camera():
    try:
        __import__("picamera")
        module = __import__("camera.camera_pi").camera_pi
    except ImportError:
        print("PiCamera module is not present")
        module = __import__("camera.camera_mock").camera_mock
    return module.Camera()


camera = init_camera()


def get_frame():
    if camera is not None:
        return camera.get_frame()
    return open("web_app.jpg", 'rb').read()


