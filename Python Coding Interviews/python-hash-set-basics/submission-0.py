from typing import List, Set


def build_hash_set(keys: List[str]) -> Set[str]:
    my_set = set()
    for key in keys:
        my_set.add(key)
    return my_set


def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    # taking in a hash set 
    # and a list of keys 
    # returns a list of booleans to determine if each key exists in the hash set 

    true_or_fasle = []

    for key in keys:
        if key in hash_set:
            true_or_fasle.append(True)
        else:
            true_or_fasle.append(False)
    return true_or_fasle 


# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))         # check the type of the output
print(sorted(list(output1))) # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"]) 
print(type(output2))         # check the type of the output
print(sorted(list(output2))) # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']))
print(check_keys({'a', 'c'}, ['d', 'c']))
