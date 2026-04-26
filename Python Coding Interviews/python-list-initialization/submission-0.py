from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    # SIZE, INDEX, VALUE AS THE PARAMS
    # WE NEED TO CREATE A LIST AND RETURN IT AS THE VARIABLE SIZE 
    # ALL THE VALUES IN THE LIST SHOULD BE 0
    # EXCEPT THE VALUE AT THE INDEX NAMED INDEX
    # THAT ONE SHOULD BE THE VARIBALE NAME VALUE

    arr = [0] * size 
    arr[index] = value
    return arr


# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
