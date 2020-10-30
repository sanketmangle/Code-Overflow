# A function to check if a number is an odd or an even number
def check_number(number):
    if (number % 2) == 0:
        print(f"The number {number} is an even number.")
    else:
        print(f"The number {number} is an odd number.")

        
print("Check if your number is even or odd.")
num = int(input("Enter a number: "))
check_number(num)
