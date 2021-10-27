
class Game:

    def __init__(self, nombre, vidas_restantes, word):
        self._nombre = nombre
        self._attempts = vidas_restantes
        self._word = word
        self._array_letters = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def attempts(self):
        return self._attempts

    @attempts.setter
    def attempts(self, value):
        self._attempts = value

    @property
    def word(self):
        return self._word

    @property
    def array_letters(self):
        return self._array_letters

    @array_letters.setter
    def array_letters(self, value):
        self._array_letters = value