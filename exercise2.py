sout = input("Enter a string: ")
lowercase = ""
uppercase = ""

for char in sout:
    if char.islower():
        lowercase += char
    elif char.isupper():
        uppercase += char

result = lowercase + uppercase
print(result)
