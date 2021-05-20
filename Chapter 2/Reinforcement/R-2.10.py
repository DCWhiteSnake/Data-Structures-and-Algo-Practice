class Vector:
    """Represent a vector in a multidimensional space """
    def __init__(self,d):
        """Create a d-dimensional vector of zeroes."""
        self._coords = [0] * d
        
    def __len__(self):
        """ Return the dimension  of the vector."""
        return len(self._coords)
    
    def __getitem__(self, j):
        """Return the jth coordinate of the vector."""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val
    
    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):        # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for d in range(len(self)):
            result[j] = self[j] + other[j]
            
    def __eq__(self,other):
        """Return true if vector has some coordinates as other."""
        return self._coords == others._coords
    
    def __ne__(self,other):
        """Return True if vector differs from other."""
        return not self == other            # rely on existing __eq__ definition
    
    def __st__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'        # adapt list representation

    def __neg__(self):
        """Return the negation of the vector"""
        for x in range(len(self._coords)):
            if self[x] not in [0, None]:
                self[x] = -self[x]
            else:
                self[x] = 0
           

if __name__ == '__main__':
    v = Vector(4)
    v[0] = 6
    -v
    print(v[0])