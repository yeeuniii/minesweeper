from game import Game


def init_game():
    try:
        game = Game(int(input("Input height\n")),
                    int(input("Input width\n")),
                    int(input("How many landmines?\n")))
        game.init_map()
        return game
    except:
        print("input error")


def run():
    game = init_game()
    game.print_map()


run()
