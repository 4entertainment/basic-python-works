"""
1.3
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""


def minmax(data):

    min = data[0]
    max = data[0]

    for i in data:
        if i > max:
            max = i

    for j in data:
        if j < min:
            min = j

    return min,max


if __name__ == "__main__":

    sequence = input("Enter a sequence of numbers separated by spaces: ")
    numbers = sequence.split()
    numbers = [int(num) for num in numbers]

    result = minmax(numbers)

    print("Min number:",result[0])
    print("Max number:", result[1])
