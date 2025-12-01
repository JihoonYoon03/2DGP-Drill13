from pico2d import *

class Ball:
    image = None
    def __init__(self, x, y):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')

        self.x, self.y = x, y
        self.w, self.h = Ball.image.w, Ball.image.h

    def update(self):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, self.w, self.h, self.x, self.y)

    def get_bb(self):
        return self.x - self.w // 2, self.y - self.h // 2, self.x + self.w // 2, self.y + self.h // 2

    def handle_collision(self, group, other):
        pass