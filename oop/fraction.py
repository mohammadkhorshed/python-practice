# Define a custom Fraction data type to represent and operate on rational numbers

class Fraction:
    
    def __init__(self, n, d = 1):
        if d == 0:
            raise ValueError("Denominator cannot be zero!")
        gcd = self.find_gcd(n ,d)
        self.num = int(n / gcd)
        self.den = int(d / gcd)
    
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __str__(self):
        return f"{self.num}" if self.den == 1 else f"{self.num}/{self.den}"
    
    @staticmethod
    def find_gcd(n, d):
        """Finds the Greatest Common Divisor (GCD) of numerator and denominator."""

        return abs(n) if d == 0 else Fraction.find_gcd(d, n % d)
    
    def float_to_fraction(self, other: float):
        """Converts a float to a Fraction by removing the decimal and simplifying."""

        num_str = str(other)
        if "." in num_str:
            decimal_places = len(num_str.split(".")[1])
        else:
            decimal_places = 0
        other_num = other * (10 ** decimal_places)
        other_den = 10 ** decimal_places
        gcd = Fraction.find_gcd(other_num, other_den)
        return Fraction(int(other_num / gcd), int(other_den / gcd))
    
    def to_float(self):
        return self.num / self.den

    def __add__(self, other):
        """Adds a Fraction to another Fraction, float, or int."""

        if isinstance(other, Fraction):
            temp_num = self.num * other.den + other.num * self.den
            temp_den = self.den * other.den
        elif isinstance(other, float):
            other = self.float_to_fraction(other)
            temp_num = self.num * other.den + other.num * self.den
            temp_den = self.den * other.den
        elif isinstance(other, int):
            temp_num = self.num + other * self.den
            temp_den = self.den
        else:
            raise TypeError("Unsupported type for operation with Fraction")
        gcd = Fraction.find_gcd(temp_num, temp_den)
        return Fraction(int(temp_num / gcd), int(temp_den / gcd))
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        """Subtracts a Fraction float, or int from another Fraction"""

        if isinstance(other, Fraction):
            temp_num = self.num * other.den - other.num * self.den
            temp_den = self.den * other.den
        elif isinstance(other, float):
            other = self.float_to_fraction(other)
            temp_num = self.num * other.den - other.num * self.den
            temp_den = self.den * other.den
        elif isinstance(other, int):
            temp_num = self.num - other * self.den
            temp_den = self.den
        gcd = Fraction.find_gcd(temp_num, temp_den)
        return Fraction(int(temp_num / gcd), int(temp_den / gcd))
    
    def __rsub__(self, other):
        return Fraction(other) - self
    
    def __mul__(self, other):
        """Multiplies a Fraction with another Fraction, float, or int."""

        if isinstance(other, Fraction):
            temp_num = self.num * other.num
            temp_den = self.den * other.den
        elif isinstance(other, float):
            other = self.float_to_fraction(other)
            temp_num = self.num * other.num
            temp_den = self.den * other.den
        elif isinstance(other, int):
            temp_num = self.num * other
            temp_den = self.den             
        gcd = Fraction.find_gcd(temp_num, temp_den)
        return Fraction(int(temp_num / gcd), int(temp_den / gcd))
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        """Divides a Fraction by another Fraction, float or int."""

        if isinstance(other, Fraction):
            temp_num = self.num * other.den
            temp_den = self.den * other.num
        elif isinstance(other, float):
            other = self.float_to_fraction(other)
            temp_num = self.num * other.den
            temp_den = self.den * other.num
        elif isinstance(other, int):
            temp_num = self.num
            temp_den = self.den * other
        gcd = Fraction.find_gcd(temp_num, temp_den)
        return Fraction(int(temp_num / gcd), int(temp_den / gcd))
    
    def __rtruediv__(self, other):
        return Fraction(other) / self
    
    def __eq__(self, other):
        """Checks equality of a Fraction and another Fraction, float or int."""

        if isinstance(other, Fraction):
            return self.num * other.den == self.den * other.num
        elif isinstance(other, float) or isinstance(other, int):
            return self.num == self.den * other
        else:
            raise TypeError("Unsupported type for operation with Fraction")
    
    def __ne__(self, other):
        """Checks inequality of a Fraction and another Fraction, float or int."""

        if isinstance(other, Fraction):
            return self.num * other.den != self.den * other.num
        elif isinstance(other, float) or isinstance(other, int):
            return self.num != self.den * other
        else:
            raise TypeError("Unsupported type for operation with Fraction")
    
    def __lt__(self, other):
        """Does less-than comparison between a Fraction and another Fraction, float or int."""

        if isinstance(other, Fraction):
            return self.num * other.den < self.den * other.num
        elif isinstance(other, float) or isinstance(other, int):
            return self.num < self.den * other
        else:
            raise TypeError("Unsupported type for operation with Fraction")
    
    def __gt__(self, other):
        """Does greater-than comparison between a Fraction and another Fraction, float or int."""

        if isinstance(other, Fraction):
            return self.num * other.den > self.den * other.num
        elif isinstance(other, float) or isinstance(other, int):
            return self.num > self.den * other
        else:
            raise TypeError("Unsupported type for operation with Fraction")
    
    def __le__(self, other):
        """Does less-than comparison between a Fraction and another Fraction, float or int."""

        if isinstance(other, Fraction):
            return self.num * other.den <= self.den * other.num
        elif isinstance(other, float) or isinstance(other, int):
            return self.num <= self.den * other
        else:
            raise TypeError("Unsupported type for operation with Fraction")
    
    def __ge__(self, other):
        """Does greater-than comparison between a Fraction and another Fraction, float or int."""

        if isinstance(other, Fraction):
            return self.num * other.den >= self.den * other.num
        elif isinstance(other, float) or isinstance(other, int):
            return self.num >= self.den * other
        else:
            raise TypeError("Unsupported type for operation with Fraction")
    
    def __pow__(self, other):
        if isinstance(other, int):
            temp_num = self.num ** other
            temp_den = self.den ** other
            gcd = Fraction.find_gcd(temp_num, temp_den)
            return f"{int(temp_num / gcd)}/{int(temp_den / gcd)}"
        elif isinstance(other, float):
            return (self.num / self.den) ** other
        elif isinstance(other, Fraction):
            return (self.num / self.den) ** other.to_float()
        else:
            raise TypeError("Unsupported type for operation with Fraction")
    
    def sqrt(self):
        return (self.num  / self.den) ** 0.5



# Create Fraction objects and demonstrate arithmetic and comparison operations
if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(3, 4)
    z = Fraction(1)
    print(x)
    print(y)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x == y)
    print(x != y)
    print(x < y)
    print(x > y)
    print(x <= y)
    print(x >= y)
    print(x + y / x)
    print(x + z)
    print(x + 1)
    print(x + 2.1)
    print(x - 1)
    print (x - 2.1)
    print(1 + x)
    print(1 - x)
    print(0.5 / y)
    print(y ** 2)
    print(x ** 1.5)
    print(Fraction.to_float(x))
    print(x.sqrt())
