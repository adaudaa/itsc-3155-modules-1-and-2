n = int(input("Enter a number : "))
float_list = []
for i in range(n):
    float_input = float(input(f"Enter number {i + 1}: "))
    float_list.append(float_input)
mean = sum(float_list) / n
print("List :", float_list)
print("Average:", mean)