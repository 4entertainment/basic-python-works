"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""
from combination import generate_combinations
def main():
    input_string = input("Enter numbers separated by spaces: ")
    num_list = input_string.split()
    num_list = [int(num) for num in num_list]  # Convert string elements to integers if needed
    print("List:", num_list)


    combination_list = generate_combinations(num_list)
    print("Combinations count with odd numbers in {}:".format(num_list),combination_list)

    oddlist = []

    for i in num_list:
        for j in num_list:
            if i*j % 2 != 0 and i != j:
                print('Pairs:{} , {}'.format(i, j))

if __name__ == "__main__":
    main()