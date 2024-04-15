from app.Card import Card


class Deck:
    def __init__(self):
        self.content = []
        self._shuffle()

    def sort(self):
        self.content = sorted(self.content)

    def draw(self):
        if self._is_empty():
            raise ValueError("Cannot draw from empty deck.")
        return self.content.pop()

    def __str__(self):
        return " ".join(str(card) for card in self.content)

    def _is_empty(self):
        return not self.content

    def _shuffle(self):
        self.content = []
        while len(self.content) != 24:
            card = Card.random()
            if card not in self.content:
                self.content.append(card)
