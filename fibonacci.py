
def fib(n):
    """Finds the nth element of the Fibonacci sequence."""
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


length_of_sequence = int(input("Enter the length of the Fibonacci sequence: "))

if length_of_sequence <= 0:
    print("Error! Number must be non zero and non negative!")
    exit(-1)

fib_sequence = []
for i in range(1, length_of_sequence + 1):
    fib_sequence.append(str(fib(i)))

print("Fibonacci sequence of {} elements: {}.".format(length_of_sequence, ", ".join(fib_sequence)))
