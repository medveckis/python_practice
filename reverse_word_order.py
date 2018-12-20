
def get_string():
    return input("Give me a string: ")


def reverse_str(string):
    words = string.split()
    words.reverse()
    return " ".join(words)


user_str = get_string()
print(f"Original string: '{user_str}'.")
print(f"Reversed string: '{reverse_str(user_str)}'.")
