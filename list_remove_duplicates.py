
from random import sample


def remove_duplicates(l):
    return list(set(l))


names = ['Sarah', 'John', 'Micheal', 'Sarah', 'Leonid', 'John']
print(f"Original list: {names}.")
print(f"List after removing duplicates: {remove_duplicates(names)}")
