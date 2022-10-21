from turtle import width
from numpy import number

n = 17

# decimal = []
# octal = []
# hexadecimal = []
# binary = []

# for i in range(1, n+1):
#     acc = 0
#     decimal.append(i)
#     octal.append(str(oct(i))[2:])
#     hexadecimal.append(str(hex(i))[2:])
#     binary.append(str(bin(i))[2:])
#     acc += 1

def print_formatted(number):
    space = len(bin(n))-2
    for i in range(1, number+1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i).upper()[2:]
        binary = bin(i)[2:]
        print(f"{decimal.rjust(space,' ')} {octal.rjust(space,' ')} {hexadecimal.rjust(space,' ')} {binary.rjust(space,' ')}")
    return

print_formatted(17)