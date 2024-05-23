class Rational:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, Rational):
            b = self.b * other.b
            a = (self.a * other.b) + (self.b * other.a)
            return Rational(a, b)
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Rational):
            b = self.b * other.b
            a = (self.a * other.b) - (self.b * other.a)
            return Rational(a, b)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Rational):
            b = self.b * other.b
            a = self.a * other.a
            return Rational(a, b)
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, Rational):
            b = self.b * other.a
            a = self.a * other.b
            return Rational(a, b)
        else:
            return None

    def __eq__(self, other):
        result = 0
        if isinstance(other, Rational):
            if self.b == other.b:
                result = self.a - other.a
            else:
                a1 = self.a * other.b
                a2 = self.b * other.a
                result = a1 - a2

            if result == 0:
                return True
            else:
                return False
        else:
            return None

    def __lt__(self, other):
        result = 0
        if isinstance(other, Rational):
            if self.b == other.b:
                result = self.a - other.a
            else:
                a1 = self.a * other.b
                a2 = self.b * other.a
                result = a1 - a2

            if result < 0:
                return True
            else:
                return False
        else:
            return None

    def __gt__(self, other):
        result = 0
        if isinstance(other, Rational):
            if self.b == other.b:
                result = self.a - other.a
            else:
                a1 = self.a * other.b
                a2 = self.b * other.a
                result = a1 - a2

            if result > 0:
                return True
            else:
                return False
        else:
            return None

    def __str__(self):
        return f"Дріб: {self.a} / {self.b} \n"
