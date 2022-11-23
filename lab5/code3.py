def fizz(num):
    if num % 3 == 0 and '3' not in str(num) or\
            num % 3 != 0 and '3' in str(num):
        return "Fizz"
    return num


def buzz(num):
    if num % 5 == 0 and '5' not in str(num) or\
            num % 5 != 0 and '5' in str(num):
        return "Buzz"
    return num


def fizzbuzz(num):
    if (num % 5 == 0 and '5' not in str(num) or
            num % 5 != 0 and '5' in str(num) and
        num % 3 == 0 and '3' not in str(num) or
            num % 3 != 0 and '3' in str(num)):
        return "FizzBuzz"
    else:
        return num
