# Print out every prime number between 1 and 1000.

for prime in range(1, 1001):
    if prime % 2 != 0:
        print(prime)