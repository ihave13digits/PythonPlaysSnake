#!/usr/bin/python3

# Classic Console Engine by digits version 1.0.2019.12

from random import randint

from display import *
from player import *
from event import *
from timer import *
from draw import Draw

class Engine:

    def __init__(self):
        self.running = True
        self.display = Display(32, 32)
        self.tick_rate = 10
        self.clock = Clock()
        self.clock.set_fps(self.tick_rate)
        self.sprites = []
        self.action_limit = 0
        self.food_limit = 1
        self.action_queue = []
        self.player = None
        self.floor = Draw(0, 0, 0)
        self.walls = Draw(10, 10, 10)

        self.red_apples = 0
        self.gold_apples = 0

        self.gold_chance = 90

        self.walls.rect(0, 0, self.display.width, self.display.height)
        self.floor.rect(1, 1, self.display.width-2, self.display.height-2)
        
    def perform_action(self):
        K = Keys()
        # Add Keypress to Action Queue
        self.event()
        actn = self.action_queue[0]

        ### Add Key Events Here ###

        if actn == "w":
            self.player.velocity = Vector2(0, -1)
        if actn == "s":
            self.player.velocity = Vector2(0, 1)
        if actn == "a":
            self.player.velocity = Vector2(-1, 0)
        if actn == "d":
            self.player.velocity = Vector2(1, 0)

        if actn == K.ESC:
            self.running = False
        
        # Clears Action Queue
        if len(self.action_queue) > self.action_limit:
            self.action_queue.pop(0)

    def event(self):
        # Get Key Press
        sel = Event.keypress()#get_key(f=str)

        self.action_queue.append(sel)

    def draw_sprites(self):
        for s in self.walls.sprites:
            self.display.draw_sprite(s)
        for s in self.floor.sprites:
            self.display.draw_sprite(s)
        if len(self.sprites) > 0:
            for s in self.sprites:
                self.display.draw_sprite(s)
        for pos in self.player.segments:
            self.display.draw(pos.x, pos.y, 0, 255, 0, 128, "██")

    def draw_square(self, X, Y, w, h, r, g, b, a, c):
        for y in range(h):
            for x in range(w):
                self.display.draw(x+X, y+Y, r, g, b, a, c)

    def update(self):
        #if self.player.last_state != Vector2(self.player.segments[-1].x, self.player.segments[-1].y):
        self.player.last_state = Vector2(self.player.segments[-1].x, self.player.segments[-1].y)
        self.player.move()
        self.player.position += self.player.velocity
        for i, f in enumerate(self.sprites):
            if self.player.segments[-1] == self.sprites[i].position:
            #if self.player.last_state == self.sprites[i].position:
                if self.sprites[i].matrix[0].color.g > 0:
                    self.gold_apples += 1
                else:
                    self.red_apples += 1
                self.player.grow()
                self.sprites.remove(f)
        self.add_food()

        p = self.player.position
        if (p.x == 0 or p.x == self.display.width-1) or (p.y == 0 or p.y == self.display.height-1):
            self.restart()

        in_self = False
        for i in range(len(self.player.segments)-2):
            if self.player.segments[i] == p:
                in_self = True

        if in_self:
            self.restart()

    def add_food(self):
        roll = randint(0, 100)
        if roll >= self.gold_chance:
            color = Color(255, 255, 0, 255)
        else:
            color = Color(255, 0, 0, 255)

        if len(self.sprites) < self.food_limit:
            food = Sprite(randint(2, self.display.width-4), randint(2, self.display.height-4), 1, 1)
            food.fill(color.r, color.g, color.b, color.a, "██")
            self.sprites.append(food)

    def restart(self):
        self.sprites.clear()
        self.start()

    def start(self):
        self.player = Player()
        self.player.position = Vector2(randint(2, self.display.width-4), randint(2, self.display.height-4))
        self.add_food()
        
        fps_set = False
        food_set = False
        settings = False
        selecting = True
        while selecting:
            time.sleep(0.06)
            self.display.clear()
            print("(1) New Game")
            print("(2) Settings")
            print("(0) Quit")

            sel = Event.keypress()
            if sel == "1":
                selecting = False
                self.run()
            if sel == "2":
                settings = True
            if sel == "0":
                self.running = False
                break

        # Settings
            while settings == True:
                time.sleep(0.06)
                self.display.clear()
                print("(1) FPS Cap")
                print("(2) Food Cap")

                sel = Event.keypress()
                if sel == "1":
                    settings = False
                    fps_set = True
                if sel == "2":
                    settings = False
                    food_set = True

            # Settings Menus
                while fps_set == True:
                    time.sleep(0.06)
                    self.display.clear()
                    print("Enter desired FPS.")
                    self.clock.set_fps(float(input(": ")))
                    fps_set = False

                while food_set == True:
                    time.sleep(0.06)
                    self.display.clear()
                    print("Enter maximum food.")
                    self.food_limit = int(input(": "))
                    food_set = False

    def run(self):
        while self.running:
            self.perform_action()
            self.update()
            self.clock.tick()
            self.display.refresh()
            # Draw Here
            self.draw_sprites()
            # Game Frame
            self.display.render()
            print("Score: {} FPS: {} Elapsed Time: {}".format(int(self.red_apples + (self.gold_apples * 5)), int(self.clock.fps), int(self.clock.elapsed)))
            print("({}, {}) ".format(self.player.last_state.x, self.player.last_state.y), end="")
            print("({}, {}) ".format(self.player.segments[-1].x, self.player.segments[-1].y), end="")
            #for i in range(len(self.player.segments)):
            #    print("({}, {}) ".format(self.player.segments[i].x, self.player.segments[i].y), end="")

E = Engine()
E.start()
