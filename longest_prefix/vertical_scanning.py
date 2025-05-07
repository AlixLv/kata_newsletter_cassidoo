# Write a function that takes a list of strings and 
# returns the longest string that is a prefix of at least two strings in the list.


def longest_common_prefix(lst: list[str])-> str:
    if len(lst) == 0:
        return ""
    
    try:
        # longueur plus court mot comme référence de limite pour la comparaison
        min_length = min(len(word) for word in lst)

        
        for index in range(min_length):
            # première lettre du premier mot comme référence
            letter = lst[0][index]
            
            for word in lst:
                if word[index] != letter:
                    return lst[0][:index]
            
        # si tous les mots sont identiques jusqu'à la longueur de référence:
        return lst[0][:min_length]
    
    except TypeError as e:
        print(f"an error occured: {e}. Int value are not accepted! You must enter string input")
             
    

if __name__ == "__main__":
    examples_list = [
        ["flower","flow","flight"], 
        ["dog","racecar","car"], 
        ["interstellar","internet","internal","interval"],
        ["abc", "abcd", "abcde"]
        ]
    
    for lst in examples_list:
        res = longest_common_prefix(lst)
        print(f"res: {res}")
       
        
    # output: "fl", "", "inter", "abc"
    
 
    