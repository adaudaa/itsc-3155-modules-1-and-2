row_number = int(input("Enter a row from 1 to 5: "))
column_number = int(input("Enter a col from 1 to 5: "))

if 1 <= row_number <= 5 and 1 <= column_number <= 5:
    grid = [[0 for _ in range(5)] for _ in range(5)]
    grid[row_number - 1][column_number - 1] = 1
    for row in grid:
        print(" ".join(map(str, row)))
else:
    print("Row and col numbers must be between 1 and 5.")
