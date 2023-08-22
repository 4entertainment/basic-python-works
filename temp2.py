"""
1.2
R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators * % /
"""

# recursive
def even(k):
    if k == 0:
        return True
    elif k == 1:
        return False
    else:
        return even(k - 2)

"""
ef even(k):
    # Check the least significant bit of the binary representation
    if (k & 1) == 0:
        return True
    else:
        return False
"""



if __name__ == "__main__":
    k = int(input("Give an integer number:"))
    answer = even(k)
    print(answer)
