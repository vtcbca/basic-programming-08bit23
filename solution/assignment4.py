def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

string = input("Enter a string: ")
reversed_string = reverse_string_recursive(string)
print(f"Reversed string: {reversed_string}")