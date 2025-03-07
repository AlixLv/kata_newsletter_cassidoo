# Make a translation function for the NATO phonetic alphabet. Extra credit: Get creative with the variants!

#Example:

# > natoify('hello world')
# > "Hotel Echo Lima Lima Oscar (space) Whiskey Oscar Romeo Lima Delta"

# > natoify('3spooky5me')
# > "Three Sierra Papa Oscar Oscar Kilo Yankee Five Mike Echo"

def natoify(chain):
    translation = []
    
    for char in chain:
        if char == " ":
            translation.append("(space)") 
        elif char in numbers:
            translation.append(numbers[char])  
             
        for key, value in nato.items():
            if char == key:
                translation.append(value)                  
      
    str_translation = " ".join(translation)
    
    return str_translation


nato = {
    "a": "Alfa",
    "b": "Bravio",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Vixtor",
    "w": "Whiskey",
    "x": "Xray",
    "y": "Yankee",
    "z": "Zulu",
}

numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}


def main():
    result = natoify('3spooky5me')
    print(result)

main()