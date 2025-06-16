def is_valid_traffic_sequence(my_list: list[str]) -> bool:
    valid_transitions = {
        "red": "green",
        "green": "yellow",
        "yellow": "red"
    }
    
    if len(my_list) <= 0:
        return False
    
    return all(
        valid_transitions[current] == next_state
        for current, next_state in zip(my_list, my_list[1:])
    )
    


if __name__ == "__main__":
    my_tests = [
        ["red", "yellow", "green"],
        ["red", "green", "yellow", "red", "green", "yellow"], 
        []
    ]

    for test in my_tests:
        res = is_valid_traffic_sequence(test) 
        print(res)   
    
