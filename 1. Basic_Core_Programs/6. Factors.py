"""
6. Factors
    Desc -> Computes the prime factorization of N using brute force.
    a. I/P -> Number to find the prime factors
    b. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
    c. O/P -> Print the prime factors of number N.
"""

def prime_factors():
    num = int(input("Enter a number to find the Prime Factor: "))
    print("Prime Factors are: ")
    for i in range(1, num+1):
        if i*i <= num:
            if num%i == 0:
                print(i)

prime_factors()
