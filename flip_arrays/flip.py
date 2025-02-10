def flip(table, direction):
    if type(table) == list:
        match direction:
            case "horizontal":
                new_table = []
                for tab in table:
                    new_tab = []
                    for val in tab:
                        new_tab.insert(0, val)
                    new_table.append(new_tab)  
            case "vertical":
                new_table = []
                for tab in table:
                    new_table.insert(0, tab)   
            case _:
                return "Input is not valid!"         
        return new_table
    else:
        return "Input is not a list!"


def main():
    my_table = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    
    result = flip(my_table, "horizontal")
    print(result)


main()    