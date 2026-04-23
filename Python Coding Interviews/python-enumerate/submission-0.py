from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for index, occurence in enumerate(nums):
        # index=[0,2, 3, 4, 5, 6, 7, 8, 9, 10]
        # occurence=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        # enumerated = [0,1],[1,2],[2,3][3,4][4,5][5,6][6,7][7,8]
        if occurence == 7:
            return index
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
   first_index = None
   for index, number in enumerate(nums):
    if number == 7:
        if first_index is None:
            first_index = index
        else:
            return index - first_index



# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
