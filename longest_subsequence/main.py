# Given a list of integers, write a function that finds the longest subsequence where the difference between 
# consecutive elements is either 1 or -1. Return the length of this subsequence.

# > longestSubsequence([1,2,3,4,5])
# 5
# > longestSubsequence([4,2,3,1,5])
# 2
# > longestSubsequence([10,11,7,8,9,12])
# 3


def get_longest_sub(lst):
    len_lst = len(lst)
    
    try:
        for sub in range(len_lst - 1):
            current_len_sub = len(lst[sub])
            print("🥕 ", lst[sub], "len: ", current_len_sub)
                
            compared_list = lst[sub + 1]
            compared_len_sub = len(compared_list)
            print("🥒 ", compared_list, "len: ", compared_len_sub)
                
            if compared_len_sub > current_len_sub:
                longest_sub = compared_len_sub
                print("🐙 ", longest_sub)
            else:  
                longest_sub = current_len_sub
                print("🪼 ", longest_sub)     
            
        return longest_sub
    except:
        print("An error occured")
    

def longest_subsequence(list):
    list_subsequences = []
    subsequence = []
    len_list = len(list)

    try:
        for i in range(len_list - 1):
            print("🌼 ", list[i])
            if list[i] + 1 == list[i + 1] or list[i] - 1 == list[i + 1]:
                print("🍁 ", list[i + 1])
                if list[i] not in subsequence:
                    subsequence.append(list[i])
                subsequence.append(list[i + 1])
                print("🍋 ", subsequence)
            else:
                list_subsequences.append(subsequence)
                print("🥬 ", list_subsequences)   
                subsequence = []
    
    
        len_list_subsequences = len(list_subsequences)
        print("🐸 ", len_list_subsequences)
        
        if len_list_subsequences == 0:
            print("🦁 ", len(subsequence))
            return len(subsequence)
        
        else:
            longest_sub =  get_longest_sub(list_subsequences)
            return longest_sub

    except:
        print("An error occured")


def main():
    #length_subsequence =  longest_subsequence([10,11,7,8,9,12])
    #print(length_subsequence)
    res = get_longest_sub([])
    print("🐼 ", res)


main()    