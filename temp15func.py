def has_values(arr):
    return len(arr) > 0


def unique_list(input_list):
    unique_items = set()
    new_unique_list = []

    for num in input_list:
        if num not in unique_items:
            unique_items.add(num)
            new_unique_list.append(num)

    return new_unique_list


def function1(list):
    dist = False
    same_numbers = []
    size1 = len(list)

    for i in range(size1):
        for j in range(i + 1, size1):
            if list[i] == list[j]:
                dist = True
                same_numbers.append(list[i])

    unique_same_numbers = unique_list(same_numbers)

    if dist:
        print("The array has same values. Same values:", unique_same_numbers)
    else:
        print("The array has all different values")

# function()
