from liczby_zespolone import Complex
import re


def menu():
    print("Which operation would you like to perform? (pick a number)\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Quit\n")
    opcode = int(input())
    while opcode not in range(1,6):
        opcode = int(input("Please select a number  from 1 to 5\n"))
    if opcode == 5:
        exit(0)
    z1 = input("Enter the first complex number in the following format: a+bj\n")
    while not re.match(r'\d+(\.\d*)?[\+\-]\d+(.\d*)?[ij]', z1):
        z1 = input("Incorrect format. Enter the number again in the following format: a+bj\n")
    z2 = input("Enter the second complex number in the following format: a+bj\n")
    while not re.match(r'\d+(\.\d*)?[\+\-]\d+(.\d*)?[ij]', z2):
        z1 = input("Incorrect format. Enter the number again in the following format: a+bj\n")
    return z1, z2, opcode

if __name__ == "__main__":
    while True:
        z1, z2, opcode = menu()
        if opcode == 1:
            result = Complex(z1) + Complex(z2)
        elif opcode == 2:
            result = Complex(z1) - Complex(z2)
        elif opcode == 3:
            result = Complex(z1) * Complex(z2)
        elif opcode == 4:
            result = Complex(z1) / Complex(z2)
        print(f"\nRESULT: {result}\n\n")




