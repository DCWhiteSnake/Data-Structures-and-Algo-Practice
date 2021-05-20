class Vector:
    """Represent a vector in a multidimensional space """
    def __init__(self,d):
        if isinstance(d,(int)):
            self._coords = [0] * d
        if isinstance(d, (list)):
            self._coords = d
        """Create a d-dimensional vector of zeroes."""
        
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
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __add__(other, self):
        """Return sum of two vectors."""
        if isinstance(other, (Vector, list)):
            if len(self) != len(other):        # relies on __len__ method
                raise ValueError('dimensions must agree')
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] + other[j]
            return result           
            
    def __eq__(self,other):
        """Return true if vector has some coordinates as other."""
        return self._coords == others._coords
    
    def __ne__(self,other):
        """Return True if vector differs from other."""
        return not self == other            # rely on existing __eq__ definition
    
    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'        # adapt list representation

    def __neg__(self):
        """Return the negation of the vector"""
        for x in range(len(self._coords)):
            if self[x] not in [0, None]:
                self[x] = -self[x]
            else:
                self[x] = 0

    def __mul__(self, other):
        """Returns a new Vector with coordinates that are 3 times the
        the respective coordinates of v

        number    number to multiply respective coordinate by
        """

        if isinstance(other, (int)):
            result = Vector(len(self))
            for x in range(len(self)):
                result[x]= other*self[x]

        elif isinstance(other, (Vector)):
            result = 0
            if len(other) != len(self):
                raise ValueError("The vector lengths must be equal")
            elif len(other) == len(self):
                for x in range(len(self)):
                    result += other[x] * self[x]

        return result

  

       
        

if __name__ == '__main__':
    v = Vector(5)
    w = Vector(5)
    v[2] = 20
    w[2] = 2
    z = v * w

    p = v * 5
    print(v)
    print(w)
    print(z)
    print(p)
            

    

