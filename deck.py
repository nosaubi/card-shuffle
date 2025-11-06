import random
import math


class Deck:
    items = []

    def new_deck(self, include_jokers=False):
        suits = ["s", "d", "c", "h"]
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        if include_jokers:
            self.items = ["JK", "JK"]
        else:
            self.items = []
        for suit in suits:
            for card in cards:
                self.items.append(f"{card}{suit}")
            if suit == "d":
                cards.reverse()

    def _draw(self):
        if len(self.items) > 0:
            return self.items.pop(math.floor(len(self.items) * random.random()))
        else:
            return "No Cards"

    def __str__(self):
        if len(self.items) == 0:
            return "No Cards"
        index = 0
        output = ""
        while index < len(self.items):
            if index == 0:
                output = self.items[index]
            elif index == len(self.items) - 1:
                output = output + ", and " + self.items[index]
            else:
                output = output + ", " + self.items[index]
            index = index + 1
        return f"Cards: {output}."

    def __repr__(self):
        num_of_cards = len(self.items)
        return f"{num_of_cards} cards"

    def __init__(self):
        self.items = []

    def shuffle(self):
        shuffled = []
        while len(self.items) > 0:
            shuffled.append(self._draw())
        self.items = shuffled

    def draw(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            return "No Cards"
