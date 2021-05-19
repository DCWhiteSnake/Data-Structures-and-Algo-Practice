from abc import ABCMeta, abstractmethod


class Sequence(metaclass = ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""


    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""


    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:                              # leftmost match
                return j
        raise ValueError('value not in sequence')           # never found matchh

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:                              # found a match
                k += 1
        return k

    def __eq__(self, other):
        """Returns True precisely when self and other are element by element equivalent."""
        return self == other


    def __it__(self, other):
        """Similiar to __eq__ but supports Lexicographic comparison (less than)."""
         equivalencies = []
        if(len(self) == len(other) and isinstance(other, (Sequence))):
            for x in range(len(self)):
                    equivalences.append(self[x] == other[x])
            if equivalences.contains(False):
                return False
            elif not (equivalencies.containes(False)):
                return True
                    
        return False
    
            
            
                              


    
