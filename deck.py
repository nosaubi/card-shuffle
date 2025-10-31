import random
import math

class Deck:
    items = []

    def new_deck(self):
        self.items = ["As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "10s", "Js", "Qs", "Ks"]

    def draw(self):
        if len(self.items) > 0:
            return self.items.pop(math.floor(len(self.items) * random.random()))
        else:
            return "No Cards"
