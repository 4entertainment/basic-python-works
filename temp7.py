"""
R-1.7 Give a single command that computes the sum from Exercise R-1.6, 
relying on Python’s comprehension syntax and the built-in sum function.
"""

n = int(input("Give a number:"))
print(sum(i*i for i in range(1,n+1) if i % 2 != 0))
