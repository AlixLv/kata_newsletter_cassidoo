def min_assembly_time(info:list[dict])->int:
    if len(info) == 1 and len(info[0]) > 0:
        return info[0]["assemblyHours"]
    elif len(info) == 1:
        return 0
    elif len(info) <= 0:
        raise ValueError("You entered an empty list")
    elif not isinstance(info, list):
        raise TypeError("You must enter a list")
    
    total = 0
    max_delivery_time = 0
    assembly_hours_max_day = 0
    
    for element in info:
        temp = element["arrivalDays"]
        if temp > max_delivery_time:
            max_delivery_time = temp
            assembly_hours_max_day = element["assemblyHours"]
    
    print(f"max: {max_delivery_time} - assembly hours on max day: {assembly_hours_max_day}")        
    total = (24 * max_delivery_time) + assembly_hours_max_day
    return total     
            
            
if __name__ == "__main__":
    res = min_assembly_time([
    { "name": "keycaps", "arrivalDays": 1, "assemblyHours": 2 },
    { "name": "switches", "arrivalDays": 2, "assemblyHours": 3 },
    { "name": "stabilizers", "arrivalDays": 0, "assemblyHours": 1 },
    { "name": "PCB", "arrivalDays": 1, "assemblyHours": 4 },
    { "name": "case", "arrivalDays": 3, "assemblyHours": 2 }
    ])
    print(f"total minimum hours: {res}")   