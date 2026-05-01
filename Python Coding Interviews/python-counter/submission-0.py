from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    # we have two string which are represented in the params
    # it shoud return a counter object that counts the frequency of each character in bot os the strings combined

    counter = Counter(s1)
    counter.update(s2)

    return counter
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
