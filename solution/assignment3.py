def fibonacci_while_loop(max_value):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= max_value:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

max_value = int(input("Enter the maximum value: "))
fib_seq = fibonacci_while_loop(max_value)
print(f"Fibonacci sequence up to {max_value}: {fib_seq}")
