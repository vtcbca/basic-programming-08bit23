def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

number = int(input("Enter a number: "))
if is_prime_recursive(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
