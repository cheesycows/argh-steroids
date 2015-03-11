
import pygame
import math
import random

import util
import sprite

# oh god why
char_points = {
    'A': [0, 0, 0.5, 1, 0.5, 1, 1, 0, 0.25, 0.5, 0.75, 0.5],
    'B': [0, 0, 0, 1, 0, 1, 0.75, 1, 0.75, 1, 1, 0.75, 1, 0.75, 
          0.75, 0.5, 0.75, 0.5, 1, 0.25, 1, 0.25, 0.75, 0, 0.75, 
          0, 0, 0, 0, 0.5, 0.75, 0.5],
    'C': [1, 0.25, 0.75, 0, 0.75, 0, 0.25, 0, 0.25, 0, 0, 0.25, 
          0, 0.25, 0, 0.75, 0, 0.75, 0.25, 1, 0.25, 1, 0.75, 1, 
          0.75, 1, 1, 0.75],
    'D': [0, 0, 0, 1, 0, 1, 0.75, 1, 0.75, 1, 1, 0.75, 1, 0.75, 
          1, 0.25, 1, 0.25, 0.75, 0, 0.75, 0, 0, 0],
    'E': [0, 1, 1, 1, 0, 0.5, 0.75, 0.5, 0, 0, 1, 0, 0, 0, 0, 1],
    'F': [0, 0, 0, 1, 0, 1, 1, 1, 0, 0.5, 0.75, 0.5],
    'G': [1, 0.75, 0.75, 1, 0.75, 1, 0.25, 1, 0.25, 1, 0, 0.75, 
          0, 0.75, 0, 0.25, 0, 0.25, 0.25, 0, 0.25, 0, 0.75, 0, 
          0.75, 0, 1, 0.25, 1, 0.25, 1, 0.5, 1, 0.5, 0.5, 0.5],
    'H': [0, 0, 0, 1, 1, 0, 1, 1, 0, 0.5, 1, 0.5],
    'I': [0.25, 1, 0.75, 1, 0.25, 0, 0.75, 0, 0.5, 0, 0.5, 1],
    'J': [0, 0, 0.5, 0, 0.5, 0, 0.5, 1, 0, 1, 1, 1],
    'K': [0, 0, 0, 1, 0, 0.5, 1, 1, 0, 0.5, 1, 0],
    'L': [0, 0, 0, 1, 0, 0, 1, 0],
    'M': [0, 0, 0, 1, 0, 1, 0.5, 0.5, 0.5, 0.5, 1, 1, 1, 1, 1, 0],
    'N': [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    'O': [1, 0.75, 0.75, 1, 0.75, 1, 0.25, 1, 0.25, 1, 0, 0.75, 
          0, 0.75, 0, 0.25, 0, 0.25, 0.25, 0, 0.25, 0, 0.75, 0, 
          0.75, 0, 1, 0.25, 1, 0.25, 1, 0.75],
    'P': [0, 0, 0, 1, 0, 1, 0.75, 1, 0.75, 1, 1, 0.75, 1, 0.75, 
          0.75, 0.5, 0.75, 0.5, 0, 0.5],
    'Q': [1, 0.75, 0.75, 1, 0.75, 1, 0.25, 1, 0.25, 1, 0, 0.75, 0, 
          0.75, 0, 0.25, 0, 0.25, 0.25, 0, 0.25, 0, 0.75, 0, 0.75, 
          0, 1, 0.25, 1, 0.25, 1, 0.75, 0.75, 0.25, 1, 0],
    'R': [0, 0, 0, 1, 0, 1, 0.75, 1, 0.75, 1, 1, 0.75, 1, 0.75, 
          0.75, 0.5, 0.75, 0.5, 0, 0.5, 0.75, 0.5, 1, 0],
    'S': [0, 0.25, 0.25, 0, 0.25, 0, 0.75, 0, 0.75, 0, 1, 0.25, 
          1, 0.25, 0.75, 0.5, 0.75, 0.5, 0.25, 0.5, 0.25, 0.5, 0, 
          0.75, 0, 0.75, 0.25, 1, 0.25, 1, 0.75, 1, 0.75, 1, 1, 0.75],
    'T': [0, 1, 1, 1, 0.5, 1, 0.5, 0],
    'U': [0, 1, 0, 0.25, 0, 0.25, 0.25, 0, 0.25, 0, 0.75, 0, 0.75, 
          0, 1, 0.25, 1, 0.25, 1, 1],
    'V': [0, 1, 0.5, 0, 0.5, 0, 1, 1],
    'W': [0, 1, 0, 0, 0, 0, 0.5, 0.5, 0.5, 0.5, 1, 0, 1, 0, 1, 1],
    'X': [0, 0, 1, 1, 1, 0, 0, 1],
    'Y': [0, 1, 0.5, 0.5, 0.5, 0.5, 1, 1, 0.5, 0.5, 0.5, 0],
    'Z': [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    '1': [0, 0.75, 0.5, 1, 0.5, 1, 0.5, 0, 0, 0, 1, 0],
    '2': [1, 0, 0, 0, 0, 0, 0.75, 0.5, 0.75, 0.5, 1, 0.75, 1, 0.75, 
          0.75, 1, 0.75, 1, 0.25, 1, 0.25, 1, 0, 0.75],
    '3': [0, 0.75, 0.25, 1, 0.25, 1, 0.75, 1, 0.75, 1, 1, 0.75, 1, 
          0.75, 0.75, 0.5, 0.75, 0.5, 1, 0.25, 1, 0.25, 0.75, 0, 
          0.75, 0, 0.25, 0, 0.25, 0, 0, 0.25, 0.25, 0.5, 0.75, 0.5],
    '4': [0.75, 0, 0.75, 1, 0.75, 1, 0, 0.25, 0, 0.25, 1, 0.25],
    '5': [1, 1, 0, 1, 0, 1, 0, 0.5, 0, 0.5, 0.75, 0.5, 0.75, 0.5, 
          1, 0.25, 1, 0.25, 0.75, 0, 0.75, 0, 0, 0],
    '6': [1, 0.75, 0.75, 1, 0.75, 1, 0.25, 1, 0.25, 1, 0, 0.75, 0, 
          0.75, 0, 0.25, 0, 0.25, 0.25, 0, 0.25, 0, 0.75, 0, 0.75, 
          0, 1, 0.25, 1, 0.25, 0.75, 0.5, 0.75, 0.5, 0, 0.5],
    '7': [0, 1, 1, 1, 1, 1, 0.25, 0],
    '8': [0, 0.75, 0.25, 1, 0.25, 1, 0.75, 1, 0.75, 1, 1, 0.75, 1, 
          0.75, 0.75, 0.5, 0.75, 0.5, 1, 0.25, 1, 0.25, 0.75, 0, 
          0.75, 0, 0.25, 0, 0.25, 0, 0, 0.25, 0, 0.25, 0.25, 0.5, 
          0.25, 0.5, 0, 0.75, 0.25, 0.5, 0.75, 0.5],
    '9': [0, 0.25, 0.25, 0, 0.25, 0, 0.75, 0, 0.75, 0, 1, 0.25, 1, 
          0.25, 1, 0.75, 1, 0.75, 0.75, 1, 0.75, 1, 0.25, 1, 0.25, 
          1, 0, 0.75, 0, 0.75, 0.25, 0.5, 0.25, 0.5, 1, 0.5],
    '0': [1, 0.75, 0.75, 1, 0.75, 1, 0.25, 1, 0.25, 1, 0, 0.75, 0, 
          0.75, 0, 0.25, 0, 0.25, 0.25, 0, 0.25, 0, 0.75, 0, 0.75, 
          0, 1, 0.25, 1, 0.25, 1, 0.75, 0.75, 1, 0.25, 0],
}

for key in char_points:
    old = char_points[key]
    char_points[key] = [old[i:i + 2] for i in range(0, len(old), 2)]

for key in char_points:
    old = char_points[key]
    char_points[key] = [[-1 * (x - 0.5), y - 0.5] for x, y in old]

class Character(sprite.Sprite):
    # drawable text object
    def __init__(self, world, character, position, scale = 20):
        super(Character, self).__init__(world)
        self.scale = scale
        self.angle = 180
        self.position = position
        self.character = character
        self.points = char_points[character]
        self.angular_velocity = 0
        self.continuous = False

    def collide(self, other):
        self.angular_velocity = random.random() * 2 - 1
        super(Character, self).collide(other)

    def update(self):
        if abs(self.angular_velocity) > 0.01:
            self.angle += self.angular_velocity
        super(Character, self).update()

    @classmethod
    def string(cls, world, string, position, scale = 20):
        kern = 2.5
        x = position[0] - len(string) * scale * kern / 2.0
        y = position[1]
        for ch in string:
            if ch in char_points:
                pos = [x, y]
                Character(world, ch, pos, scale)
            x += scale * kern

def draw_string(surface, string, colour, scale, position, 
                centre = False, angle = 0):
    kern = 2.5
    x = position[0]
    y = position[1]
    a = scale * util.cos(angle)
    b = scale * -util.sin(angle)
    c = -b
    d = a
    if centre:
        x -= a * kern * len(string) / 2.0
        y -= c * kern * len(string) / 2.0
    for ch in string:
        if ch in char_points:
            screen = [[-a * u - b * v + x, -c * u - d * v + y] 
                      for u, v in char_points[ch]]
            for i in range(0, len(screen), 2):
                pygame.draw.line(surface, util.WHITE, screen[i], screen[i + 1])
        x += a * kern
        y += c * kern

