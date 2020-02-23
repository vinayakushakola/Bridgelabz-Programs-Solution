"""
2. Sum of three Integer adds to ZERO
    Desc -> A program with cubic running time. Read in N integers and
            counts the number of triples that sum to exactly 0.
    a. I/P -> N number of integer, and N integer input array
    b. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
    c. O/P -> One Output is number of distinct triplets as well as
              the second output is to print the distinct triplets.
"""

def sum_of_3_add_to_0(array, N):
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if array[i] + array[j] + array[k] == 0:
                    count += 1
                    print(array[i], array[j], array[k])
    print("Number of Distinct Triplets:", count)


def start():
    N = int(input("Enter number of elements you want in an Array: "))
    elements = []
    for i in range(N):
        elements.append(int(input()))
    sum_of_3_add_to_0(elements, N)

start()
