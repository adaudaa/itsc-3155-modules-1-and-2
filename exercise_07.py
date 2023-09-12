all_numbers = []
even_numbers = []

while True:
    user_input = input("Enter a number or QUIT to quit: ")
    if user_input == "QUIT":
        break

    try:
        num = int(user_input)
        all_numbers.append(num)
        if num % 2 == 0:
            even_numbers.append(num)
    except ValueError:
        print("Please enter a valid integer or type 'QUIT'.")
print("All nums:", all_numbers)
print("Even nums:", even_numbers)
