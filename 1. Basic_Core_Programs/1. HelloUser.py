"""
1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
    a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
    b. Logic -> Replace <<UserName>> with the proper name
    c. O/P -> Print the String with User Name
"""

username = input("Enter your name: ")
print("Hello "+username+", How are you?")