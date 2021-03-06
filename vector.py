#!/usr/bin/python3

class Direction2D:

    def __init__(self, step=1, sx=1, sy=1):
        self.step = Vector2(sx, sy)
        self.n = Vector2(0, -step)
        self.s = Vector2(0, step)
        self.e = Vector2(-step, 0)
        self.w = Vector2(step, 0)

        self.ne = Vector2(-step, -step)
        self.nw = Vector2(step, -step)
        self.se = Vector2(-step, step)
        self.sw = Vector2(step, step)

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Binary Operators

    def __add__(self, i):
        return Vector2((self.x + i.x),(self.y + i.y))

    def __sub__(self, i):
        return Vector2((self.x - i.x),(self.y - i.y))

    def __mul__(self, i):
        return Vector2((self.x * i.x),(self.y * i.y))

    def __truediv__(self, i):
        return Vector2((self.x / i.x),(self.y / i.y))
    
    def __floordiv__(self, i):
        return Vector2((self.x // i.x),(self.y // i.y))

    def __mod__(self, i):
        return Vector2((self.x % i.x),(self.y % i.y))

    def __pow__(self, i):
        return Vector2((self.x ** i.x),(self.y ** i.y))

    def __lshit__(self, i):
        return Vector2((self.x << i.x),(self.y << i.y))

    def __rshift__(self, i):
        return Vector2((self.x >> i.x),(self.y >> i.y))

    def __and__(self, i):
        return Vector2((self.x & i.x),(self.y & i.y))

    def __xor__(self, i):
        return Vector2((self.x ^ i.x),(self.y ^ i.y))

    def __or__(self, i):
        return Vector2((self.x | i.x),(self.y | i.y))

    # Extended Assignments

    def __iadd__(self, i):
        self.x += i.x
        self.y += i.y
        return Vector2(self.x, self.y)

    def __isub__(self, i):
        self.x -= i.x
        self.y -= i.y
        return Vector2(self.x, self.y)

    def __imul__(self, i):
        self.x *= i.x
        self.y *= i.y
        return Vector2(self.x, self.y)

    def __itruediv__(self, i):
        self.x /= i.x
        self.y /= i.y
        return Vector2(self.x, self.y)

    def __ifloordiv__(self, i):
        self.x //= i.x
        self.y //= i.y
        return Vector2(self.x, self.y)

    def __imod__(self, i):
        self.x %= i.x
        self.y %= i.y
        return Vector2(self.x, self.y)

    def __ipow__(self, i):
        self.x **= i.x
        self.y **= i.y
        return Vector2(self.x, self.y)

    def __ilshit__(self, i):
        self.x <<= i.x
        self.y <<= i.y
        return Vector2(self.x, self.y)

    def __irshift__(self, i):
        self.x >>= i.x
        self.y >>= i.y
        return Vector2(self.x, self.y)

    def __iand__(self, i):
        self.x &= i.x
        self.y &= i.y
        return Vector2(self.x, self.y)

    def __ixor__(self, i):
        self.x ^= i.x
        self.y ^= i.y
        return Vector2(self.x, self.y)

    def __ior__(self, i):
        self.x |= i.x
        self.y |= i.y
        return Vector2(self.x, self.y)

    # Unary Operators

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __pos__(self):
        return Vector2(+self.x, +self.y)

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __invert__(self):
        return Vector2(~self.x, ~self.y)

    def __complex__(self):
        return Vector2(complex(self.x), complex(self.y))

    def __int__(self):
        return Vector2(int(self.x), int(self.y))

    def __long__(self):
        return Vector2(long(self.x), long(self.y))

    def __float__(self):
        return Vector2(float(self.x), float(self.y))

    def __oct__(self):
        return Vector2(oct(self.x), oct(self.y))

    def __hex__(self):
        return Vector2(hex(self.x), hex(self.y))

    # Comparison Operators

    def __lt__(self, i):
        if (self.x < i.x and self.y <= i.y) or (self.x <= i.x and self.y < i.y):
            return Vector2(self.x, self.y)

    def __le__(self, i):
        if self.x <= i.x and self.y <= i.y:
            return Vector2(self.x, self.y)

    def __eq__(self, i):
        if self.x == i.x and self.y == i.y:
            return Vector2(self.x, self.y)

    def __ne__(self, i):
        if self.x != i.x or self.y != i.y:
            return Vector2(self.x, self.y)

    def __ge__(self, i):
        if self.x >= i.x and self.y >= i.y:
            return Vector2(self.x, self.y)

    def __gt__(self, i):
        if (self.x > i.x and self.y >= i.y) or (self.x >= i.x and self.y > i.y):
            return Vector2(self.x, self.y)

    # Misc.

    def coords(self):
        return Vector2(self.x, self.y)

