from itertools import combinations

def odds(numbers_list):
    odd_count = 0
    for num in numbers_list:
       if num%2 != 0:
         odd_count+=1
    print("odd number size in {}: {}".format(numbers_list,odd_count))
    return odd_count



def generate_combinations(data):
    # data = [1, 2, 3, 4]
    # r = 2  # Size of combinations
    r = odds(data)
    combinations_list = list(combinations(data, r))

    print(combinations_list)
