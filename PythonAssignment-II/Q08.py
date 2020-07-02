# Write a function, is_prime, that takes an integer and returns True if the number is prime and False if the number is not prime.

def is_prime(number):
    if number >1:
        for n in range(2,number):
            if (number % n) == 0:
                return False
        else:
            return True

    else:
        return False

print(is_prime(7))