from itertools import product

def odd_sum(a, b):
    a_odd = [x for x in a if x % 2 == 1]
    a_even = [x for x in a if x % 2 == 0]
    b_odd = [x for x in b if x % 2 == 1]
    b_even = [x for x in b if x % 2 == 0]
    
    return list(product(a_odd, b_even)) + list(product(b_odd, a_even))


if __name__ == "__main__":
    res = odd_sum([9, 14, 6, 2, 11], [8, 4, 7, 20])
    print(res)