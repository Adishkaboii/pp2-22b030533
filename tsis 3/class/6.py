def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())

numbers = list(range(2, n+1))


primes = list(filter(lambda x: is_prime(x), numbers))


print(primes)
