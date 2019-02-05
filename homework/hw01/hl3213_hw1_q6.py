class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0]*d
        elif isinstance(d, list):
            self.coords = [d[i] for i in range(d)]
    
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

    #========NEW METHODS=======
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for k in range(len(self)):
            result[k] = other[k] - self[k]
        return result
    
    def __neg__(self):
        result = Vector(len(self))
        for l in range(len(self)):
            result[l] = self[l] * -1
        return result

    def __mul__(self, other):
        if isinstance(other, int):
            result = Vector(len(self))
            for m in range(len(self)):
                result[m] = self[m] * other
            return result
        elif isinstance(other, Vector):
            return
    
    def __rmul__(self, other):
        return 
    #==========================
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)


v1 = Vector(5)
v1[1] = 10
v1[-1] = 10
print(v1)