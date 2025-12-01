from pico2d import *

import game_world
from game_world import *
import common

class Ball:
    image = None
    def __init__(self, x, y):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')

        self.x, self.y = x, y
        self.w, self.h = Ball.image.w, Ball.image.h

        add_collision_pair('boy:ball', None, self)

    def update(self):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.clip_draw(0, 0, self.w, self.h, sx, sy)
        min_x, min_y, max_x, max_y = self.debug_bb(sx, sy)
        draw_rectangle(min_x, min_y, max_x, max_y)

    def get_bb(self):
        return self.x - self.w // 2, self.y - self.h // 2, self.x + self.w // 2, self.y + self.h // 2

    def debug_bb(self, sx, sy):
        return sx - self.w // 2, sy - self.h // 2, sx + self.w // 2, sy + self.h // 2

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)