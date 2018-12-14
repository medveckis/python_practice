
check = int(input("Enter number for checking: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_fiv = []
for el in a:
    if el < check:
        less_than_fiv.append(str(el))

result = " ".join(less_than_fiv)
print(result)
