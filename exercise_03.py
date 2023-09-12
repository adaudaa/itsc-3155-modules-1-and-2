n = int(input("Enter an integer greater than 1: "))
if n <= 1:
    print("Invalid input. Please enter an integer greater than 1.")
else:
    for i in range(n + 1):
        cube = i ** 3
        print(f"The cube of {i} is {cube}")
