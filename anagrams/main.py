# Given two strings, s and p, return an array of all the start indices of p's anagrams in s.

# Examples:
# findAnagrams("cbaebabacd", "abc")
# > [0, 6]

# findAnagrams("fish", "cake")
# > []

# findAnagrams("abab", "ab")
# > [0, 1, 2]


def findAnagrams(s, p):
    try:
        p_set = set(p)
        max_length = len(p)
        current_part = ""
        index_lst = []
        
        for indice, value in enumerate(s):
            # on récupère la sous-partie de s à comparer avec p:
            start_indice = indice
            end_indice = indice + max_length
            
            if end_indice > len(s):
                pass  
            else:
                current_part = s[start_indice:end_indice]
                print(f"current part: {current_part}")
                
                # on compare les lettres communes entre sous-partie de s avec p:
                if len(set(current_part) & p_set) == max_length and len(p_set) != 0:
                    print(set(current_part) & p_set)
                    index_lst.append(start_indice)
                else:
                    pass
        
        return index_lst  
    
    except TypeError:
        raise TypeError("Enter a valid string please")
    except:
        print("Enter a string please")    


res = findAnagrams("cbaebabacd", "abc")  
print(res)  
    
        


