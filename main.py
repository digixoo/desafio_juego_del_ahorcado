import Entity.Game
import Game.Print
import IO.data
import random

def run():
    words = IO.data.bulk_data()
    word_index= random.randint(0, len(words)- 1)

    print(f'parala escogida: {words[word_index]}')

    game = Entity.Game.Game('Juego del quemado', 5, words[word_index])
    engine = Game.Print.screen(game)

    engine.start()



if __name__ == '__main__':
    run()