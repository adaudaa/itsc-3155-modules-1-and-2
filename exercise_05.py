list1 = []
list2 = []
for i in range(5):
    num = int(input(f"Enter a number for the first list:"))
    list1.append(num)

for i in range(5):
    num = int(input(f"Enter a number for the second list:"))
    list2.append(num)
common_values = list(set(list1) & set(list2))
print("\nFirst List:", list1)
print("Second List:", list2)
print("Common List:", common_values)
