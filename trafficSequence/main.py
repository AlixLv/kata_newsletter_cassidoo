#Given an array of strings representing a sequence of traffic light states ("red" for stop, "green" for go, "yellow" for slow), 
# write a function that returns true if the sequence could represent a valid state machine for a standard traffic light. 
# The only valid transitions are: red to green, green to yellow, and yellow to red.


def is_valid_traffic_sequence(my_list:list[str])->bool:  
    valid_transitions = {
    "red":"green",
    "green":"yellow",
    "yellow":"red"
    }  
    
    for i in range(len(my_list)-1):
        if valid_transitions[my_list[i]] != my_list[i+1]:
            return False   
    return True      


if __name__ == "__main__":
    #result = is_valid_traffic_sequence(["red", "yellow", "green"])
    result = is_valid_traffic_sequence(["red", "green", "yellow", "red", "green", "yellow"])
    print(f"🩷 {result}")