
from random import sample

nums = sample(range(100), 10)
print(nums)


def get_list_ends(l):
    return [l[i] for i in range(len(l)) if i == 0 or i == len(l) - 1]


list_ends = get_list_ends(nums)
print(list_ends)
