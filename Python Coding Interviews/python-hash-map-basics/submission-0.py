from typing import List, Dict


def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    # keys = passes key
    # values = passed values
    # Taking two lists and returning a dictionary to combine the key:value from the lists

    my_dictionary = {}

    for key, value in zip(keys,values):
        my_dictionary[key] = value
    return my_dictionary



def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    # hashmap 
    # keys
    # returning a list 
    # based on the parameters identify what is happening 

    values = []

    for key in keys:
        value = hash_map[key]
        values.append(value)
    return values


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
