
import random

a = random.sample(range(0, 100), 15)
b = random.sample(range(0, 100), 10)
print("a: ", a)
print("b: ", b)

if len(a) > len(b):
    res_list = list(set(a).intersection(set(b)))
else:
    res_list = list(set(b).intersection(set(a)))

result = " ".join([str(i) for i in res_list])
if not result:
    result = "none"
print("Intersection two of this lists: {}.".format(result))
