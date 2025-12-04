import random
import math

#import the deck with import game and new_deck = game.Deck().
class Deck:
    items = []

    def _draw(self):
        if len(self.items) > 0:
            return self.items.pop(math.floor(len(self.items) * random.random()))
        else:
            return "No Cards"

    def shuffle(self):
        shuffled = []
        while len(self.items) > 0:
            shuffled.append(self._draw())
        self.items = shuffled

    def deal(self, number_to_draw = 1, number_of_hands = 2):
        if number_of_hands == 0:
            return Deck(self.draw(number_to_draw))
        return [Deck(self.draw(number_to_draw)) for _ in range(number_of_hands)]

    #make a new deck with new_deck.new_deck(False, 1, 2) and check it ith print(new_deck)
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

        self.shuffle()

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

    def __init__(self, starting_cards = []):
        if not isinstance(starting_cards, list):
            print("Wrong format input a list")
            return None
        self.items = starting_cards

    #use new_deck.draw() to draw (X) cards
    def draw(self, number_to_draw = 1):
        if len(self.items) == 0:
            return "No Cards"
        if number_to_draw > len(self.items):
            return f"{len(self.items)} cards left"
        return [self.items.pop(0) for _ in range(number_to_draw)]

    def game(self, players = 1, cards = 1):
        deck = Deck()
        while True:
            discard = []
            deck.new_deck(False)
            print("new game")
            if players < 1:
                return "must have at least one player"
            hands = [[]for _ in range(players)]
            for c in range(players):
                drawn_cards = deck.draw(cards)
