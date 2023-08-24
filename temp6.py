"""
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""
def odd_squares(number):
    list = []
    sum = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            sum+= i*i
            list.append(i*i)

    return list,sum


if __name__ == "__main__":
    n = int(input("Give a number:"))

    result = odd_squares(n)
    print("List:",result[0])
    print("Sum:",result[1])




