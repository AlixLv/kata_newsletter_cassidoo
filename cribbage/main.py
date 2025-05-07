def main():
    # score = scoreHand(ex1)
    # print("🌈 ", score)
    score = get_sum_score([7,8,5, "J", "K"])
    print("SCORE: ", score)


def scoreHand(cards_list):
    cards = clean_list(cards_list)
    score = 0
    sum = 0
    consecutive_ranks = 0
    
    for index in range(len(cards) - 1):
        try:
            card = cards[index]            
            pair = get_pair(index, card, cards)
            print("🐞 ", pair)
            if pair is not None:
                score += 1
                  
        except ValueError:
            print("Is not an int!")    
    
    consecutive_ranks = get_consecutive_rank(cards_list, cards_order)
    print("🦋 consecutive rank: ", consecutive_ranks)
    
    if consecutive_ranks is not None and len(consecutive_ranks) >= 3:
        score += len(consecutive_ranks)        
    return score


def clean_list(cards_list):
    new_list = []
    
    for card in cards_list:
        try: 
            if card[0] in faces_cards:
                number = card[0]
                new_list.append(number)

            else:    
                number = int(card[0])
                new_list.append(number)
                
        except:
            print("Something went wrong!")        
    #print("🌱 new list", new_list)    
    return new_list    


def get_sum_score(cards_list):
    sum = 0
    score = 0
    
    #get all the possible combinations in the list (2, 3, 4, and 5 cards combinations)
    #calculate sum for each combinations
    # score+= 2 if sum == 15x
    
    
         
    return score


def get_consecutive_rank(cards_list, cards_order):
    try:
        score = 0
        start_index = cards_order.index(cards_list[0])
        #print("🦞 ", start_index)
        part_list = slice(start_index, len(cards_order))
        list_comparing = cards_order[part_list]
        #print("🐬 sliced list: ", list_comparing)
        
        for i, j in zip(list_comparing, cards_list):
            print("i: ", i, " j: ", j)
            if i == j:
                score += 1
            else:
                break    
                   
    except:
        print("Error!")    
    return score


def get_pair(start_index, start_card, cards_list):
    pair = []
    for card in range(start_index + 1, len(cards_list)):
        try:
            comparing_card = cards_list[card]
            print("🍊 ", start_card, comparing_card)
            if start_card == comparing_card:
                pair.append(start_card)
                pair.append(comparing_card)
                print("🐸 ", pair)
            else:
                continue     
        except ValueError:
            print("Not same type value!")

    
    if len(pair) > 1:    
        return pair     
    else:
        return None
                             
    
faces_cards = {
    "A": 1,
    "K": 10,
    "J": 10
}

cards_order = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

ex1 = ["7H", "8C", "9D", "JH", "KS"] #5
ex2 = ["AH", "2C", "3D", "4S", "5H"] #7



if __name__ == "__main__":
    main()   