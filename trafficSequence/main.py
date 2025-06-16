#Given an array of strings representing a sequence of traffic light states ("red" for stop, "green" for go, "yellow" for slow), 
# write a function that returns true if the sequence could represent a valid state machine for a standard traffic light. 
# The only valid transitions are: red to green, green to yellow, and yellow to red.


def is_valid_traffic_sequence(input_list:list[str])->bool:  
    valid_transitions = {
    "red":"green",
    "green":"yellow",
    "yellow":"red"
    }  
    
    if len(input_list) <= 1:
        return False
    elif not isinstance(input_list, list):
        raise TypeError("You must enter a list")
    

    my_list = []
    for word in input_list:
        if not isinstance(word, str):
            raise TypeError("You must enter a list of string")
        my_list.append(word.lower())

    
    for i in range(len(my_list)-1):
        if valid_transitions[my_list[i]] != my_list[i+1]:
            return False   
    return True      


if __name__ == "__main__":
    my_tests = [
        ["red", "yellow", "green"],
        ["red", "green", "yellow", "red", "green", "yellow"], 
        [],
        ["Green"],
        ["Red", "Green", "Yellow"]
    ]

    for test in my_tests:
        result = is_valid_traffic_sequence(test)
        print(f"🎯 {result}")
    
    