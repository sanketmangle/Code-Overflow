# A program to calculate the power of a given number x to another number y
def check_power(x, y):
    i = 1
    power = 1
    while i <= y:
        power *= x
        i += 1
    print(f"The power of {x} to {y} is: {power}")


a = int(input("Enter a positive integer: "))
b = int(input("Enter the exponent value: "))
check_power(a, b)
