import sys
from app.Game import Game

if __name__ == "__main__":
    try:
        games_num = int(sys.argv[1])
    except IndexError:
        print("nie podano danych wejściowych")
    except ValueError:
        print("nieprawidłowe dane wejściowe")
    game = Game()
    counter = 0
    while counter < games_num and not game.get_result():
        counter += 1
        game = Game()
        game.run()
    print(game)
    print(counter)
    print(game.get_result())
