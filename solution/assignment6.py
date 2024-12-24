def print_pattern_while_loop(rows):
    i = 1
    while i <= rows:
        print(" ".join(["*"] * i))
        i += 1

rows = int(input("Enter the number of rows: "))
print_pattern_while_loop(rows)
