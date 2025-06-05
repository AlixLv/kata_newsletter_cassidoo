def nestArray(arr:list)->list[list]:
    """"
    Turn an array of integers into a nested array.
    """
    
    matrix = [arr[len(arr)-1]]

    for i in range(len(arr)-2, -1, -1):
        matrix = [arr[i], matrix]
    
    return matrix


if __name__ == "__main__":
    res = nestArray([1, 2, 3, 4,])
    print(res)
    #output : [1, [2, [3, [4]]]]