from math import sqrt as sqrt

def roots(a, b, c):
    if not a:
        raise ValueError("a must not equal 0")
    delta = b*b -4*a*c
    if delta < 0:
        raise ValueError("No real solutions. Delta is negative")
    x1 = (-b - sqrt(delta))/(2*a)
    x2 = (-b + sqrt(delta))/(2*a)
    return x1, x2

if __name__ == "__main__":
    coeffs = input("Type in a, b and c coefficients separated by spaces.\nExample:\n3 2 6\n")
    coeffs = [int(i) for i in coeffs.split(' ')]
    result = roots(*coeffs)
    print(result)