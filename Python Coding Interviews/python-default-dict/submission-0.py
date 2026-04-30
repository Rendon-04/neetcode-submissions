from ast import keyword
from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    # s is a string of a word as the param 
    # return a dictionary where the key is the character and the value is the number of time that key characters appears in the string

    char_frequency = defaultdict(int)
    for char in s:
        char_frequency[char] += 1
    return char_frequency




def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    # nums is a nested list of lists
    # returning a dictionary and the key will the first element of each list
    # the value will be the rest of the elements in that list 
    sublist_dict = defaultdict(list)

    for num in nums:
        key = num[0]
        value = num[1:]

        sublist_dict[key].extend(value)

    return sublist_dict


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
