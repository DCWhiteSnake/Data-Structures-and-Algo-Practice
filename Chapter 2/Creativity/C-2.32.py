import math 
from Progression import Progression

class ProgressionEx(Progression):
    def __init__(self, first = 65536):
        """Extends the Progression class
        each value in the progression is the square root of the previous progression
        """
        super().__init__(first)
        self._count = 0

    def _advance(self):
            self._current = math.pow(self._current, 1/2)

if __name__ == '__main__':
    px = ProgressionEx()
    px.print_progression(10)


