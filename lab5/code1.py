def fizz(num):
    if num % 3 == 0:
        return "Fizz"
    return num


def buzz(num):
    if num % 5 == 0:
        return "Buzz"
    return num


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    else:
        return num
