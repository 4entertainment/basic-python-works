"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""
from temp15func import function1

def main():
    input_string = input("Give sequence of integer values:")
    num_list = input_string.split()
    num_list = [int(num) for num in num_list]  # Convert string elements to integers if needed
    print("List:", num_list)
    function1(num_list)


if __name__ == "__main__":
    main()

