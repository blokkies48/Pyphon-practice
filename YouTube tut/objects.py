class Guitar:
    def __init__(self):
        self.n_strings = 6

    def play(self, amount):
        print('playing guitar')
        fun = int(amount) + 7
        print(fun)

my_guitar = Guitar()
print(my_guitar.n_strings)
my_guitar.play(5)

class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.n_strings = 8

    def playlouder(self):
        print('playing guitar'.upper())

my_e_guitar = ElectricGuitar()
my_e_guitar.playlouder()
print(my_e_guitar.n_strings)