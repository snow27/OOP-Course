def is_prime(n):
    is_not_prime = False
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                is_not_prime = True
    else:
        is_not_prime = True
    if is_not_prime:
        return False
    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
