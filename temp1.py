"""
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""
def is_multiple(n, m):
    if n % m == 0:  # Check if n is divisible by m without remainder
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input("n: "))
    m = int(input("m: "))
    result = is_multiple(n, m)
    print(result)