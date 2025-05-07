def is_common_prefix(length, lst):
    # slicing en python retourne jusqu'à l'indice n-1 !!
    str0, count = lst[0][:length], len(lst)  
    print(f"str0: {str0}")   
    return all(lst[index][:length] == str0 for index in range(1, count))


def longest_common_prefix(lst: list[str]) -> str:
    if not lst:
        return ""
        
    # préparation de la recherche binaire
    min_length = min(len(word) for word in lst)
    low, high = 1, min_length

    
    while low <= high:
        mid = (low + high) // 2
        print(f"mid {mid}")
        
        #vérification si un préfixe de longueur mid est commun à toutes les chaînes
        if is_common_prefix(mid, lst):
            low = mid + 1
         
        # si non, on cherche des préfixes plus courts    
        else:
            high = mid - 1
        
    return lst[0][:(low + high) // 2]            
        



if __name__ == "__main__":
    #res = longest_common_prefix(["flower","flow","flight"])
    # output: "fl"

    #res = longest_common_prefix(["dog","racecar","car"])
    # # output: ""

    res = longest_common_prefix(["interstellar","internet","internal","interval"])
    # # output: "inter"

    #res = longest_common_prefix(["abc", "abcd", "abcde"])
    # output: "abc"
    
    #res = longest_common_prefix([])
    print(f"res: {res}, {type(res)}")    
    