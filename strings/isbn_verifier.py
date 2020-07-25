import re

def cleanInput(input):
    check = input[-1]
    stub = re.sub("\\D", '', input[:len(input)-1])
    if (len(stub) == 9) & (re.match('X|\\d', check) is not None):
        return list(stub + check)
    return False

def is_valid(isbn): 
    if not(isbn):
        return False
    isbn = cleanInput(isbn)
    if not(isbn):
        return False
    total = 10 if (isbn[9] == 'X') else int(isbn[9])
    for i in range(9):
        total += (int(isbn[i]) * (10 - i))
    return (total % 11 == 0)

def isbn_13(isbn10):
    starter = ['9', '7', '8'] + cleanInput(isbn10)[:9]
    total = 0
    for i in range(12):
        weight = 1 if (i % 2 != 0) else 3
        total += (weight * int(starter[i]))
    r = 10 - (total % 10)
    check = [str(r)] if (r < 10) else ['0']
    return ''.join(starter + check)
