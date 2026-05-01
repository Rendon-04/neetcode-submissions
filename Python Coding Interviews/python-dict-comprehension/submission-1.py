from typing import List, Dict


def num_to_index(nums: List[int]) -> Dict[int, int]:
    # our param is a list of numbers
    # the keys are the elements of the list
    # values are the indices of thos elements

    number_corresponding_indices = {num: index for index, num in enumerate(nums)}
    return number_corresponding_indices


# do not modify below this line
print(num_to_index([1, 2, 3, 4, 5, 6, 7, 8]))
print(num_to_index([8, 7, 6, 5, 4, 3, 2, 1]))
print(num_to_index([0, 3, 2, 4, 5, 1]))
