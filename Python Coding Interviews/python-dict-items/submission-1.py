from typing import Dict, List, Tuple


def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    # we have a dictionary 
    # contains names as the key and age as the value
    # returns a tuple with the name and age 

    result = []

    # for key, value in age_dict.items():
    #     name_age = key, value
    #     result.append(name_age)

    for key in age_dict:
        value = age_dict[key]
        result.append((key,value))

    return result



# do not modify below this line
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}))
print(get_dict_items({'Bob': 30, 'David': 40, 'Charlie': 35, 'Alice': 25, 'Eve': 45}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45, 'Frank': 50}))
