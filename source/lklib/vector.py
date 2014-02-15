class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def __repr__(self):
        s = ""
        for i in xrange(len(self)):
            if s != "":
                s += ";"
            s += str(self[i])
        return s

    def __str__(self):
        return str(self.coords)

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Vector() can only be add to another vector.")
        if len(self) != len(other):
            raise BaseException("Vectors have different dimentions.")
        l = []
        for i in xrange(len(self)):
            l.append(self[i]+other[i])
        return Vector(*tuple(l))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Vector() can only be sub to another vector.")
        if len(self) != len(other):
            raise BaseException("Vectors have different dimentions.")
        l = []
        for i in xrange(len(self)):
            l.append(self[i]-other[i])
        return Vector(*tuple(l))

    def __mul__(self, other):
        if isinstance(other, int):
            l = []
            for i in xrange(len(self)):
                l.append(self[i]*other)
            return Vector(*tuple(l))
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise BaseException("Vectors have different dimentions.")
            s = 0
            for i in xrange(len(self)):
                s += self[i]*other[i]
            return s
        else:
            raise TypeError("Vector() can only be mul to another vector or an int.")

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * -1

    def __pow__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Vector product only defined between two vectors.")
        if len(self) != len(other) or len(other) != 3:
            raise BaseException("Vectors are not 3-dimentional.")
        return Vector(self[1]*other[2]-self[2]*other[1],
                      self[2]*other[0]-self[0]*other[2],
                      self[0]*other[1]-self[1]*other[0])

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Vector() expects an int index.")
        if 0 <= index < len(self):
            return self.coords[index]
        else:
            raise IndexError("Index is not in range.")

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Vector() expects an int index.")
        if 0 <= index < len(self):
            self.coords = list(self.coords)
            self.coords[index] = value
            self.coords = tuple(self.coords)
        else:
            raise IndexError("Index is not in range.")

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        return self[1]

    @z.setter
    def z(self, value):
        self[1] = value
