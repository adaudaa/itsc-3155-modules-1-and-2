user_input_list = []
for i in range(10):
    while True:
        try:
            num = int(input(f"Enter number {i + 1}: "))
            user_input_list.append(num)
            break
        except ValueError:
            print("Please enter a valid integer.")

unique_elements = []
for num in user_input_list:
    if user_input_list.count(num) == 1:
        unique_elements.append(num)

print("Original list:", user_input_list)
print(" Numbers that appear only once):", unique_elements)
