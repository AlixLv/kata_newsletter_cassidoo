array_of_int = [1,2,3,4,4]

def main():
    result = majority(array_of_int)
    print("RESULT: ", result)


def most_frequent(list):
    frequency = 0
    compared_frequency = 0
    number = list[0]

    for element in list:
        # compte le nombre de fois qu'apparaît l'élément dans la liste
        current_frequency = list.count(element)
        compared_frequency = current_frequency
        if compared_frequency == frequency and element != number:
            return False
        # si la fréquence trouvée est plus grande que counter, la fréquence devient la référence
        if current_frequency > frequency:
            frequency = current_frequency
            # on stocke la valeur qui revient le plus fréquemment dans number
            number = element  
    return number          


def even_or_odd(list):
    even = 0
    odd = 0
    for element in list:
        if (element % 2) == 0:
            even +=1
        else:
            odd +=1    
    print("even: ", even, " odd: ", odd)        
    if even > odd:
        return "Majority of even"
    elif odd > even:
        return "Majority of odd"   
    else:
        return "No majority"    


def majority(list):
    most_frequent_number = most_frequent(list)
    result_of_majority = even_or_odd(array_of_int)
    print("most frequent number: ", most_frequent_number)
    print("result of majority: ", result_of_majority)
    if most_frequent_number == False and result_of_majority == "No majority":
        print("IN IF")
        return result_of_majority
    elif most_frequent_number == False and result_of_majority != "No majority":
        print("IN ELIF")
        return result_of_majority
    else:    
        print("most frequent number: ", most_frequent_number)
        return most_frequent_number

main()

