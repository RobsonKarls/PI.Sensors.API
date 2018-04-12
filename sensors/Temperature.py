from random import randint

class Temperature:
    @staticmethod
    def read():
        return randint(-40,40)