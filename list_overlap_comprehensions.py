
from random import sample

list_1 = sample(range(100), 10)
list_2 = sample(range(100), 10)
print("list 1: ", list_1)
print("list 2: ", list_2)


difference_list = [str(i) for i in list_1 for j in list_2 if i == j]
# difference_list = list(map(str, set(list_1).intersection(set(list_2))))
diff_str = ", ".join(difference_list)
print("result: ", diff_str)
