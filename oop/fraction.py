# Creating a data type "Fraction"

class Fraction:
    
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator cannot be zero!")
        self.num = n
        self.den = d
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def find_gcd(self, n, d):
        return abs(n) if d == 0 else self.find_gcd(d, n % d)


    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        gcd = self.find_gcd(temp_num, temp_den)
        return Fraction(int(temp_num / gcd), int(temp_den / gcd))
    
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        gcd = self.find_gcd(temp_num, temp_den)
        return Fraction(int(temp_num / gcd), int(temp_den / gcd))
    
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        gcd = self.find_gcd(temp_num, temp_den)
        return Fraction(int(temp_num / gcd), int(temp_den / gcd))
    
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        gcd = self.find_gcd(temp_num, temp_den)
        return Fraction(int(temp_num / gcd), int(temp_den / gcd))
    
    def __eq__(self, other):
        num1 = self.num / self.den
        num2 = other.num / other.den
        return True if num1 == num2 else False
    
    def __ne__(self, other):
        num1 = self.num / self.den
        num2 = other.num / other.den
        return True if num1 != num2 else False
    
    def __lt__(self, other):
        num1 = self.num / self.den
        num2 = other.num / other.den
        return True if num1 < num2 else False
    
    def __gt__(self, other):
        num1 = self.num / self.den
        num2 = other.num / other.den
        return True if num1 > num2 else False
    
    def __le__(self, other):
        num1 = self.num / self.den
        num2 = other.num / other.den
        return True if num1 <= num2 else False
    
    def __ge__(self, other):
        num1 = self.num / self.den
        num2 = other.num / other.den
        return True if num1 >= num2 else False


# Creating new objects and performing operations to check its working
if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(3, 4)
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

