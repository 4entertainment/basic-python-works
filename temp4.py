"""
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def squares(number):
    list = []
    for i in range(1,n+1):
        list.append(i*i)

    return list


if __name__ == "__main__":
    n = int(input("Give a number:"))

    result = squares(n)
    print(result)
