class ReversedSequenceIterator:
    """ An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence             # keep a reference to the underlying
        self._k = 0                     # will increment to 0 on first call to next


    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += -1                     # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k])   # return the data element
        else:
            raise StopIteration()        # there are no more elements


    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


if __name__ == '__main__':
    sequen = [1,2,3,4,5]
    x = ReversedSequenceIterator(sequen)
    a = next(x)
    b= next(x)
    c= next(x)
    d= next(x)
    e= next(x)
    
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    
