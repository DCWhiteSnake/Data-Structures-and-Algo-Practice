from Progression import Progression
class ProgressionEx(Progression):
    """Extends the Progression Class."""

    def __init__(self, first = 2,second = 200):
        """Initialize the Progression Extension Class
        first       first number in the progression.
        second       second number in the progression.
        """
        super().__init__(first)
        self._f = first
        self._s = second
        self._count = 1
    
    def _advance(self):
        """Helper method for __next__, generates the next item."""
        if  self._count == 1:    
            self._current = self._s # If this is the first call then output second
            self._prev = self._f    # make first the previous value, for use in the next call
            self._count += 1        # increment _count
        else:
            self._prev, self._current =self._current,  abs(self._current - self._prev)

if __name__ == '__main__':
    px = ProgressionEx()
    px.print_progression(10) # output: 2 200 198 2 196 194 2 192 190 2
