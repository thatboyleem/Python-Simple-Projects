#useful tool for working with numbers, it divides one number by another number and returns the remainder
number = input("Enter a number and i'll tell you if its even or odd: ")
number = int(number)

if number%2==0:
    print(f"\n the number {number} is even")
else:
    print(f"the number {number} is odd")
