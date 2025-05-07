# Write a function that takes a list of strings and 
# returns the longest string that is a prefix of at least two strings in the list.


def longest_common_prefix(lst: list[str])-> str:
    if len(lst) == 0:
        return ""
    
    # longueurplus court mot comme référence de limite pour la comparaison
    min_length = min(len(word) for word in lst)
    print(f"mini mength: {min_length}")
    
    for index in range(min_length):
        # première lettre du premier mot comme référence
        letter = lst[0][index]
        print(f"letter: {letter}")
        
        for word in lst:
            print(f"letter in word: {word[index]}, reference letter: {letter}")
            if word[index] != letter:
                return lst[0][:index]
        
    # si tous les mots sont identiques jusqu'à la longueur de référence:
    return lst[0][:min_length]        
    
 


if __name__ == "__main__":
    res = longest_common_prefix(["flower","flow","flight"])
    # output: "fl"
    
    #res = longest_common_prefix(["dog","racecar","car"])
    # # output: ""
    
    #res = longest_common_prefix(["interstellar","internet","internal","interval"])
    # # output: "inter"
    
    #res = longest_common_prefix(["abc", "abcd", "abcde"])
    # output: "abc"
    print(f"res: {res}, {type(res)}")