
def is_prime(n):
    if n == 1:
        return False
    for divisor in range(2, n // 2):
        if n % divisor == 0:
            return False
    return True


# num = int(input("Give me a number: "))
for num in [2, 3, 5, 7, 11, 13, 97, 77, 12, 4]:
    if is_prime(num):
        print(f"The number {num} is prime.")
    else:
        print(f"The number {num} is not prime.")
