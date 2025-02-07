# Write a function that evaluates a postfix expression (also known as Reverse Polish Notation) and returns the result. 
# The expression will contain single-digit integers and the operators +, -, *, and /. 

# Examples
# evaluatePostfix('12+')
# > 3

# evaluatePostfix('56+7*')
# > 77


operators = {
    "+": lambda item1, item2: item1 + item2,
    "-": lambda item1, item2: item1 - item2,
    "/": lambda item1, item2: item1 / item2,
    "*": lambda item1, item2: item1 * item2
}


def evaluate_postfix(expression):
    notation = list(expression)
    item1 = None
    item2 = None    
    index = 0
    
    while index < len(notation):
        if index >= 2:
            item1 = int(notation[index - 1])
            item2 = int(notation[index - 2])
            print("🍊 item1: ", item1, " item2: ", item2)
             
            if notation[index] in operators:
                result = operators[notation[index]](item1, item2)
                print("🥬 ", result)
                
                characters_to_remove = [str(item1), str(item2), notation[index]]
                print("🥑 characters to remove: ", characters_to_remove)
                
                for value in characters_to_remove:
                    if value in notation:
                        notation.remove(value)
                        
                notation.insert(0, str(result))
                print("🍒 ", notation)
                # réinitialisation de l'index à 0, pour évaluer correctement toutes les valeurs de la liste notation
                index = 0
                continue
        
        index += 1  
                
    return notation[0] if notation else None


result = evaluate_postfix("43")
print("🌈 ", result, type(result))
