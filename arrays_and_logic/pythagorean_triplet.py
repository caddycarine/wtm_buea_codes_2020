def triplets_with_sum(number):
    '''
    Because a < b < c and a+b+c = number,
      -->  a cannot be greater than half of the number (else either b or c would have to be less than a)
      -->  b cannot be greater than (number-a)/2 (else b would be greater than c)
      -->  b cannot be less than a+1 (because it must be greater than a)
      -->  The minimum value of b is when c is maximum (c = number/2) hence b must be greater than (number/2)-i
    '''
    triplets = []

    for a in range(1, int(number/2)):
        b_max = int((number-a)/2)
        b_min = max(a+1, int(number/2)-a)        
        
        if (a > b_min) | (b_min > b_max):
            break
        group = [[a, b, number-a-b] for b in range(b_min, b_max+1) if is_triplet([a, b, number-a-b])]
        triplets += group
    return triplets


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    return (triplet[0]**2 + triplet[1]**2 == triplet[2]**2) & (triplet[0] < triplet[1] < triplet[2])
