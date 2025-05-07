#Given an array of characters chars, compress it such that consecutive duplicate characters 
# are replaced with the character followed by the count of duplicates. If the count is 1, omit it.

def compress(text:list[str])->list[str]:
    """
    itérer dans la liste
    vérifier si la même lettre se suit en plusieurs exemplaires
    si oui, compter le nombre d'exemplaires
    
    """
    try:
        new_list= []
        counter = 1
        
        for index in range(0, len(text)-1):
            if text[index] == text[index + 1]:
                counter += 1
                print(f"counter: {counter}, char: {text[index]}")

            else:
                if counter > 1:
                    if text[index] not in new_list:
                        print("COUCOU")
                        new_list.append(text[index])
                        new_list.append(str(counter))
                else:
                    new_list.append(text[index])
                counter = 1  
        new_list.append(text[index])
        new_list.append(str(counter))                 
        return new_list
    
    except TypeError as e:
        print(f"Invalid type input: {e}")
        raise
          

if __name__ == "__main__":
    res = compress(["a", "b", "b", "b", "a", "c", "c", "c"])
    print(f"res : {res}")
    #output: ["a", "b", "3", "c"]
    
    # res = compress(["a", "a", "b", "b", "c", "c", "c"])
    # print(f"res : {res}")
    # output: ["a", "2", "b", "2", "c", "3"]
    
    # res = compress([3, "b", "c", "c"])
    # print(f"res : {res}")
    