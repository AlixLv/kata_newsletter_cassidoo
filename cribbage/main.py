def main():
    score = scoreHand(ex1)
    print("🌈 ", score)

def scoreHand(cards_list):
    cards = cards_list.copy()
    score = 0
    sum = 0
    
    #iterating over the list, looking for numbers
    # additionning numbers to check if we get 15. Score += 2
    # checking same value number. If a pair of number score += 2
    # checking runs of 3 or more consecutive ranks. score +=1 per card 
    
    for index, card in enumerate(cards):
        try:
            number = int(card[0])
        
            if type(number) == int: 
                print("🌼 index: ", index, " number: ", number)
                sum += number
                if sum == 15:
                    print("15s!")
                    sum = 0
                    score += 2
        
        except ValueError:
            print("Is not an int!")    
    
    return score



ex1 = ["7H", "8C", "9D", "JH", "KS"] #5
ex2 = ["AH", "2C", "3D", "4S", "5H"] #7



if __name__ == "__main__":
    main()   