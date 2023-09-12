grade = int(input("Enter a grade from 0 to 100): "))
if 0 <= grade <= 100:
    if 90 <= grade <= 100:
        L_grade = 'A'
    elif 80 <= grade < 90:
        L_grade = 'B'
    elif 70 <= grade < 80:
        L_grade = 'C'
    elif 60 <= grade < 70:
        L_grade = 'D'
    else:
        L_grade = 'F'
print(f'Your grade is: {L_grade}')

