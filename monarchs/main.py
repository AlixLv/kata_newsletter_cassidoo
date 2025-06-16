#Given an array of strings representing the names of monarchs and their ordinal numbers, 
#write a function that returns the list of names sorted first by name and 
#then by their ordinal value (in Roman numerals), in ascending order.

def sort_monarchs(monarchs:list[str])->list[str]:
    if len(monarchs) <= 1:
        return monarchs
    
    if not isinstance(monarchs, list):
        raise TypeError("You must enter an input of type list")
    
    for monarch in monarchs:
        if not isinstance(monarch, str):
            raise TypeError("You must enter a list with string only")
    
    pivot = monarchs[len(monarchs) // 2]
    left = [monarch for monarch in monarchs if monarch < pivot]
    middle = [monarch for monarch in monarchs if monarch == pivot]
    right = [monarch for monarch in monarchs if monarch > pivot]
    
    return sort_monarchs(left) + middle + sort_monarchs(right)
    


if __name__ == "__main__":
    tests = [
        ["George VI", "Elizabeth I", "George V", "Elizabeth II", "George IV", "Edward VIII"], 
        ["Louis IX", "Louis VIII", "Philip II", "Philip I"],
        [],
        ["Louis IX"],
    ]
    
    for test in tests:
        res = sort_monarchs(test)
        print(res)
    