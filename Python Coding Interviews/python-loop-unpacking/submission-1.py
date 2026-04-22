"""We need to create a loop that checks both the variables in the set of the list.
   Everytime the loop runs, it has to check the current name and the current score. 
   We need a way to track the current highest score and also to place the name of the
   highest score if it is True."""

from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
 
    
    name_of_highest_scorer = ""
    highest_score = 0
    for name, score in scores:
        if score > highest_score:
            highest_score = score
            name_of_highest_scorer = name
    return name_of_highest_scorer


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
