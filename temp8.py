"""
R-1.8 Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
R-1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
mylist = []
for i in range(0,9):
    mylist.append(2**i)

mylistshortcut = [2**i for i in range(9)]
print(mylist)

print("short")

print(mylistshortcut)
