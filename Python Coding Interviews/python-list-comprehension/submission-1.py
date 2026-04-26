from typing import List


def create_list_of_odds(n: int) -> List[int]:
    # arr = []
    # for n in range(1, n + 1):
    #     if n % 2 != 0:
    #         arr.append(n)
    # return arr

    return [n for n in range(1, n + 1) if n % 2 != 0]


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
