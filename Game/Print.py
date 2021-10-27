from .util import print_underline
from Business.Logic import is_valid, win, lose

class screen:
    
    def __init__(self, game):
        self.game = game

    def start(self):
        is_finish = False
        is_win = False
        user_letters=[]

        print(f'Bienvenido a {self.game.nombre}')
        print(f'--------------------------------')
        while not is_finish:
            print(f'Cantidad de vidas restantes: {self.game.attempts}')
            print(f'Ingrese un caracter')
            letter = input()

            if is_valid(self.game.word, letter):
                print('Correcto')
                user_letters.append(letter)
            else:
                print('Incorrecto')
                self.game.attempts = self.game.attempts - 1
                
            print(f'palabra: {print_underline(self.game.word, user_letters)}')

            if win(self.game.word, user_letters):
                is_finish = True
                is_win = True
            elif lose(self.game.attempts):
                is_finish = True
            
        if is_win:
            print('felicidades ganaste')
        else:
            print('perdiste pero no te rinadas, vuelve a intentarlo')

