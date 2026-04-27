from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
# conver the list into a deque
# rotate the values in the left to the left by k steps
# return the deque 
    new_list = deque(arr)


    for _ in range(k):
        popped_variable = new_list.popleft()
        new_list.append(popped_variable)
    return new_list
        



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
