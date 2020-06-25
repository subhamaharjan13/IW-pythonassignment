# Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime(number):
    if number >1:
        for n in range(2,number):
            if (number % n) == 0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")

    else:
        print("Number is not prime")

prime(7)
