
in_str = input("Enter a string: ")
is_palindrome = True
length = range(int(len(in_str) / 2))
for index in length:
    if in_str[index] != in_str[len(in_str) - index - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("The following string '{}' is palindrome.".format(in_str))
else:
    print("The following string '{}' is not palindrome.".format(in_str))
