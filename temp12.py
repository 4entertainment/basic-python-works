"""
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
import random


input_string = input("Enter numbers separated by spaces: ")
num_list = input_string.split()
num_list = [int(num) for num in num_list]  # Convert string elements to integers if needed
print("List:", num_list)



def custom_choice(data):
    if not data:
        raise ValueError("Sequence is empty")

    index = random.randrange(len(data))
    return data[index]


# Kullanım örneği
my_list = [1, 2, 3, 4, 5]
random_element = custom_choice(my_list)
print("Random element:", random_element)
