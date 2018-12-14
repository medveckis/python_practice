
num = int(input("Enter a number: "))
divisors = []
for n in range(2, num):
    if num % n == 0:
        divisors.append(str(n))

result = ", ".join(divisors)
print("All the divisors of {} is {} (excluded 1 and {}).".format(num, result, num))
