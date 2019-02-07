class Vector:
    #__init__
    #pre: Vector, int/list
    #post: 
    #initializes a Vector with coordinates of d
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0]*d
        elif isinstance(d, list):
            self.coords = d
    
    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self, j):
        return self.coords[j]
    
    def __setitem__(self, j, val):
        self.coords[j] = val
    
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    #=============NEW METHODS============

    #__sub__
    #pre: Vector, Vector
    #post: Vector
    #gets difference between two Vector coordinates
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for k in range(len(self)):
            result[k] = self[k] - other[k]
        return result
    
    #__neg__
    #pre: Vector
    #post: Vector
    #negates the coordinates of a Vector
    def __neg__(self):
        result = Vector(len(self))
        for l in range(len(self)):
            result[l] = self[l] * -1
        return result

    #__mul__
    #pre: Vector, Vector/int
    #post: Vector
    #returns the scalar/dot product of the inputs
    def __mul__(self, other):
        if isinstance(other, int):
            result = Vector(len(self))
            for m in range(len(self)):
                result[m] = self[m] * other
            return result
        elif isinstance(other, Vector):
            if (len(self) != len(other)):
                raise ValueError('dimensions must agree')
            else:
                result = 0
                for x in range(len(self)):
                    result += self[x] * other[x]
                return result
    
    #__rmul__
    #pre: Vector, int
    #post: Vector
    #returns the scalar product of the inputs
    def __rmul__(self, other):
        result = Vector(len(self))
        for x in range(len(self)):
            result[x] = self[x] * other
        return result

    #====================================
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)