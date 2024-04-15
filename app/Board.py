from app.Deck import Deck
from app.Card import Card


class Board:
    def __init__(self):
        self.content: list[list[Card]] = []
        self.hand: Card = None
        self._place()

    def _place(self):
        deck = Deck()
        rows_counter = 0
        while rows_counter < 4:
            self.content.append([])
            cards_counter = 0
            while cards_counter < 6:
                try:
                    self.content[rows_counter].append(deck.draw())
                    cards_counter += 1
                except ValueError as e:
                    print(e)
            rows_counter += 1
        self.hand = self.content[3].pop()
        self.hand.flip()

    def replace(self):
        new_hand = self.content[self.hand.suit_idx()][self.hand.value_idx()]
        self.content[self.hand.suit_idx()][self.hand.value_idx()] = self.hand
        self.hand = new_hand
        self.hand.flip()

    def get_hand(self):
        return self.hand

    def is_face_up(self):
        return all(all(card.get_face_up() for card in row) for row in self.content)

    def __str__(self):
        string = ""
        for i in range(6):
            row = ""
            for j in range(4):
                if i == 5 and j == 3:
                    continue
                row += str(self.content[j][i]) + "\t"
            row += "\n"
            string += row
        string += "hand: " + str(self.hand) + "\n"
        return string
