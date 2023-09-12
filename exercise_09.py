word_list = []
for i in range(5):
    word = input(f"Enter a word : ")
    word_list.append(word)
resultant_string = ' '.join(word_list)

print("Words:", word_list)
print("One String:", resultant_string)
