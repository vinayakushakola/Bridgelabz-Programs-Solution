"""
5. Harmonic Number
    Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
            (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
    a. I/P -> The Harmonic Value N. Ensure N != 0
    b. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
    c. O/P -> Print the Nth Harmonic Value.
"""

# Using Recursion
def harmonic_number(n):
    if n < 2:
        return 1
    else:
        return 1/n + (harmonic_number(n-1))
print(harmonic_number(10))


def harmonic_num(n):
    harmonic = 0
    for i in range(1, n+1):
        harmonic += 1/i
    return harmonic
print(harmonic_num(10))