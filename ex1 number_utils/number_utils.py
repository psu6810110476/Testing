def is_prime(num):
    if num < 2: 
        return False

    for n in range(2, int(num**0.5) + 1):
        if num % n == 0: 
            return False
    return True

def is_prime_list(numbers):
    return [is_prime(num) for num in numbers]