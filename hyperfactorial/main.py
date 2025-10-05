def hyperfactorial(n):
    """
    Étant donné l'entier non négatif n, affichez la valeur de son hyperfactorial.
    formule de calcul: H(n) = 1¹ × 2² × 3³ × 4⁴ × ... × nⁿ
    """
    if n < 0:
        raise ValueError(f'{n} is a negative value. Please enter a value greater than 0.')
    elif not isinstance(n, int):
        raise TypeError (f'{n} is not an integer. Please enter a integer value.')
    
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i ** i
    
    return result



if __name__ == "__main__":
    res = hyperfactorial(4)
    print(f'res: {res}')