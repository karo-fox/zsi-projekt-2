from app.Board import Board
from app.Card import Card


class Game:
    def __init__(self):
        self.board: Board = Board()
        self.STOP_CARD: Card = Card("A", "♠")
        self.visualization = []
        self.is_won = False

    def run(self):
        self.visualization.append(str(self.board))
        while self.board.get_hand() != self.STOP_CARD:
            self.board.replace()
            self.visualization.append(str(self.board))
        self.check_result()

    def get_result(self):
        return self.is_won

    def check_result(self):
        if self.board.is_face_up():
            self.is_won = True

    def __str__(self):
        return "\n".join(self.visualization)
