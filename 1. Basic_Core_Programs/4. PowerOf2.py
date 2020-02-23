"""
4. Power of 2
    Desc -> This program takes a command-line argument N and prints a
            table of the powers of 2 that are less than or equal to 2^N.
    a. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
    b. Logic -> repeat until i equals N.
    c. O/P -> Print the year is a Leap Year or not
"""

N = int(input("Enter a number: "))
if 0 <= N and N < 31:
    for i in range(pow(2, N)):
        print("2 x", i, "=", (2*i))
        if (2*i)%400 == 0:
            print(2*i, "is a Leap Year\n")
        elif (2*i)%4 == 0 and (2*i)%100 != 0:
            print(2*i, "is a Leap Year\n")
        else:
            print(2*i, "is not a Leap Year\n")