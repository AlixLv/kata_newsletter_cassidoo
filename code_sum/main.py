def odd_sum(arr1, arr2):
    big_list=[]
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            new_list=[]
            sum= arr1[i]+ arr2[j]
            if sum%2 != 0:
                new_list.append(arr1[i])
                new_list.append(arr2[j])
                big_list.append(new_list)
            else:
                continue
    if len(big_list) == 0:
        return None
    return big_list            


if __name__ =="__main__":
    #res = odd_sum([9, 14, 6, 2, 11], [8, 4, 7, 20])
    res = odd_sum([2, 4, 6, 8], [10, 12, 14])
    print(res)