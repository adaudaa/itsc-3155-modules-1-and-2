user_input = input("Enter a string: ")
character_list = list(user_input)

split_lists = [character_list[i:i + 3] for i in range(0, len(character_list), 3)]
for sublist in split_lists:
    print(sublist)
