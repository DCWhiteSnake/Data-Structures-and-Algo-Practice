"""Class that mimic's the python range class."""
from timeit import timeit
class Range:
    
    def __init__(self, start,stop=None,step = 1):
        """Initialize a Range instance

        The accepted inputs are
        start    the beginning of the range
        stop     the number which to stop the iteration before
        step     the step size of the iteration
        """

        if step == 0:
            raise ValueError("step cannot be '0'")

        if stop is None:               # special case of range(n)
            start, stop = 0, start      # should be treated as if range(0,n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step -1)// step)


        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard intrepretation if negative)."""
        if k < 0:
            k += len(self)             # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step

    def __contains__(self, k):
        """Returns true if the sequence contains k"""
        if isinstance(k, (str)):
            return False
        
        else:
            x = self[(k - self._start + self._step -1)//self._step]
            if x == k:
                return True
            else:
                print(x)
                return False
        return False

if __name__ == '__main__':
    somenumbers = Range(-25,1000000000000, 10)
    if "B" in somenumbers:               
        print("Contains")
    else:
        print("Does not contain")

    if -25 in somenumbers:               
        print("Contains")
    else:
        print("Does not contain")
    if 1000000 in somenumbers:               
        print("Contains")
    else:
        print("Does not contain")
    if 20222235 in somenumbers:               
        print("Contains")
    else:
        print("Does not contain")
     
    
