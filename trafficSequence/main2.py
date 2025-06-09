def is_valid_traffic_sequence(my_list: list[str]) -> bool:
    valid_transitions = {
        "red": "green",
        "green": "yellow",
        "yellow": "red"
    }
    
    return all(
        valid_transitions[current] == next_state
        for current, next_state in zip(my_list, my_list[1:])
    )


if __name__ == "__main__":
    res = is_valid_traffic_sequence(["red", "green", "yellow", "red", "green", "yellow"]) 
    print(res)   
    
