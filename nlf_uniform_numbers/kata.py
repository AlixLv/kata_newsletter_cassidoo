# Given the current system of NFL uniform numbers, a given player's position, and an array of existing numbers on the team, 
# write a function that returns a list of numbers that the given player can choose from for their uniform.

# Example: 
# > availableNumbers("QB", [1, 2, 3, 10, 19])
# > [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18]


current_system = {
    tuple([1, 9]): ["QB", "RB", "WR", "TE", "LB", "DB", "K", "P", "LS"],
    tuple([10, 19]): ["QB", "RB", "WR", "TE", "LB", "DB", "K", "P", "LS"], 
    tuple([20, 19]): ["RB", "WR", "TE", "LB", "DB", "K", "P", "LS"],
    tuple([30, 19]): ["RB", "WR", "TE", "LB", "DB", "K", "P", "LS"],
    tuple([40, 49]): ["RB", "WR", "TE", "LB", "DB", "K", "P", "LS"],  
    tuple([50, 59]): ["OL", "DL", "LB", "LS"],
    tuple([60, 69]): ["OL", "DL", "LS"],
    tuple([70, 79]): ["OL", "DL", "LS"],
    tuple([80, 89]): ["RB", "WR", "TE", "LS"],
    tuple([90, 99]): ["DL", "LB", "K", "P", "LS"]
}

def available_numbers(position, numbers_lst):  
    final_lst = []
    
    if position == None:
        return []
    else:
        for key, value in current_system.items():
            for val in value:
                if position == val:
                    min, max = int(key[0]), int(key[1])
                    lst = is_number_available(min, max, numbers_lst)
                    final_lst.extend(lst)
                    
        return final_lst


def is_number_available(min, max, numbers_lst):
    available_lst = []
    
    try:        
        for n in range(min, max + 1):
            available_lst.append(n)
        print("🐱 ", available_lst)
            
        for number in numbers_lst:
            if number in available_lst:
                available_lst.remove(number)
            else:
                continue    
        print("🐼 ", available_lst)
              
    except:
        print("An error occured. Check your arguments.")
           
    return available_lst      


def main():
    #res = available_numbers("OL", [])
    #print("🌈 ", res)
    is_number_available(1, 10, [])
    
    
main()    
    
