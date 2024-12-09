# Function to generate prime numbers
def prime_numbers(n):
    primes = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


#  call this function with a number to get all prime numbers less than that number
print(prime_numbers(20))
# Output: [2, 3, 5, 7, 11, 13, 17, 19]
