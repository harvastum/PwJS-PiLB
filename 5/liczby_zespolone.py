class Complex():
    def __init__(self, real, imag:float=0.):
        if isinstance(real, str):
            real, imag = self._from_str(real)
        self.real = float(real)
        self.imag = float(imag)


    def _from_str(self, number):
        if '-' in number:
            parts = number.rstrip('j').rstrip('i').split('-')
            return float(parts[0]), -float(parts[1])
        parts = number.rstrip('j').rstrip('i').split('+')
        return float(parts[0]), float(parts[1])


    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return Complex(self.real + other, self.imag)
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return Complex(self.real - other, self.imag)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(
                self.real * other.real - self.imag * other.imag,
                self.real * other.imag + self.imag * other.real)
        return Complex(self.real * other, self.imag * other)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            divisor  = Complex(other.real/(other.real**2 + other.imag**2),
                            other.imag/(other.real**2 + other.imag**2))
            return self * divisor
        return Complex(self.real/other, self.imag/other)

    def __str__(self):
        return f"{self.real}{'+'+str(self.imag) if self.imag >= 0 else self.imag}j"

    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def __bool__(self):
        if self.imag == 0 and self.real == 0:
            return False
        return True

if __name__ == "__main__":
    z0 = Complex(5.6, -6.3)
    z1 = Complex('4.5-3.44j')
    z2 = Complex(5.6, 4)
    z3 = Complex('2+0j')
    print(z0, z1, z2, z3, sep='\n')

