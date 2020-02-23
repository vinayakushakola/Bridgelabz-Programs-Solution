"""
3. Leap Year
    a. I/P -> Year, ensure it is a 4 digit number.
    b. Logic -> Determine if it is a Leap Year.
    c. O/P -> Print the year is a Leap Year or not
"""

def check_leap_year():
    year = int(input("Enter a year: "))
    if year % 400 == 0:
        print(year, "is a Leap Year")
    elif year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")

check_leap_year()

