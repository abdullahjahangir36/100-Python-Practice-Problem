# Print first 25 prime numbers
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_first_n_primes(n):
    primes = []
    num = 2  # Start checking for prime numbers from 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Number of primes to find
n = 25
# Find and print the first 25 prime numbers
prime_numbers = print_first_n_primes(n)
print(f"The first {n} prime numbers are:")
print(prime_numbers)
