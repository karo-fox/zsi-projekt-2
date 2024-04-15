import random


class Card:
    SUIT = ("♥", "♦", "♣", "♠")
    VALUE = ("9", "10", "J", "Q", "K", "A")

    def __init__(self, value, suit):
        if value not in self.VALUE or suit not in self.SUIT:
            raise ValueError("Unrecognized card value or suit.")
        self.value = value
        self.suit = suit
        self.is_up = False

    def flip(self):
        self.is_up = not self.is_up

    def suit_idx(self):
        return self.SUIT.index(self.suit)

    def value_idx(self):
        return self.VALUE.index(self.value)

    def get_face_up(self):
        return self.is_up

    def __str__(self):
        if not self.is_up:
            return "XXX"
        return self.value + self.suit

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other):
        if self.suit == other.suit:
            return self.value_idx() > other.value_idx()
        return self.suit_idx() > other.suit_idx()

    @classmethod
    def random(cls):
        return Card(random.choice(cls.VALUE), random.choice(cls.SUIT))
