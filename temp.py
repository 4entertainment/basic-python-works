"""
Write a short Python function that counts the number of vowels in a given
character string.
"""
from typing import List

input = input("give your sentence:")

list = ["A","E","I","İ","O","Ö","U","Ü"]
i = 0
output_list: List[str] = []


for char in input:
        if char.upper() in list:
            i=i+1
            if char not in output_list:  # Check if the vowel is already in the list
                output_list.append(char)

print("Count of vowels: ", i ,"\n Output: ",output_list)