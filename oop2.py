import operator as op

class Vector:
    def __init__(self, *v):
        self._v = list(v)

    def __repr__(self):
        return __class__.__name__ + repr(tuple(self._v))
    
    def __add__(self, right):
        return Vector(*map(op.add, self._v, right._v))
    
    def __sub__(self, right):
        return Vector(*map(op.sub, self._v, right._v))
    
    def __iadd__(self, right):
        self._v[:] = map(op.add, self._v, right._v)
        return self

    def __len__(self):
        return len(self._v)

    def __getitem__(self, index):
        if type(index) == int:
            return self._v[index]
        elif type(index) == slice:
            return Vector(*self._v[index])
        else:
            raise TypeError(f"Index must be int or slice, not {type(index)}")
    
    def __setitem__(self, index, value):
        if type(index) == int:
            self._v[index] = value
        elif type(index) == slice:
            self._v[index] = value if not isinstance(value, Vector) else value._v[:]
        else:
            raise TypeError(f"Index must be int or slice, not {type(index)}")