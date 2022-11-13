def exp(base, power = 2):
    return base ** power

def calc(num, val):
    if val == 'a':
        return exp(exp(num))
    elif val == 'b':
        res = exp(num, 3)
        if res <= 100:
            return res
    else:
        return 'Illegal value'

if __name__ == '__main__':
    print(calc(7 , 'd'))
