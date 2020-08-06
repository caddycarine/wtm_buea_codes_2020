def classify(number):
    if not (number > 0):
        raise ValueError('Number must be natural.')
    factors = [f for f in range(1, number) if number%f == 0]
    aliquot = sum(factors)
    if aliquot == number:
        return 'perfect'
    if aliquot < number:
        return 'deficient'
    return 'abundant'
