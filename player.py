#!/usr/bin/python3

from vector import *

class Player:

    def __init__(self):
        self.position = Vector2(2, 2)
        self.velocity = Vector2(0, 0)
        self.segments = []
        self.last_state = self.position

        self.segments.append(self.position)


    def grow(self):
        self.segments.append(self.last_state)

    def move(self):
        self.segments.pop(0)
        self.segments.append(self.position)
