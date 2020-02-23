"""
1.  2D Array
    Desc -> A library for reading in 2D arrays of integers, doubles, or booleans
            from standard input and printing them out to standard output.
    a. I/P -> M rows, N Cols, and M * N inputs for 2D Array.
    b. Logic -> create 2 dimensional array in memory to read in M rows and N cols
    c. O/P -> Print 2 Dimensional Array.
"""

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter your entries\n")

TwoDArray = []
for i in range(rows):
    r = []
    print("For", i+1, "row")
    for j in range(cols):
        r.append(int(input()))
    TwoDArray.append(r)

for i in range(rows):
    for j in range(cols):
        print(TwoDArray[i][j], end=" ")
    print()
