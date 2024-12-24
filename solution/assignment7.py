def print_triangle_while_loop(n):
    i = 1
    while i <= n:
        print(" " * (n - i), end="")
        j = 1
        while j <= (2 * i - 1):
            print(j, end=" ")
            j += 1
        print()
        i += 1

n = int(input("Enter the number of rows: "))
print_triangle_while_loop(n)
