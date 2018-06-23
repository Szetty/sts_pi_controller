class Camera(object):
    image = "web_app.jpg"

    def get_frame(self):
        return open(self.image, 'rb').read()
