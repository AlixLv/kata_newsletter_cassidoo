def toggle_char(text:str)->str:
    alpabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"," x", "y", "z"]
    new_string = ""
    temp = ""
    
    for car in text:
        temp = car
        if temp.lower() in alpabet:
            isitupper = car.isupper()
            print(f"🍎 temp: {temp}")
            print(f"⭐️ isitupper: {isitupper}")
            if isitupper == True:
                temp = temp.lower()
                new_string += temp
                temp = ""
            else:
                temp = temp.upper()
                new_string += temp
                temp = ""
        else:
            new_string += temp            
        
    
    return new_string
         

if __name__ == "__main__":
    res = toggle_char("HeheHeheHEheheHeH")
    print(f"🌈{res}🌈")

# > "hELLO, WORLD!"
# toggleChar("HeheHeheHEheheHeH")
# > "hEHEhEHEheHEHEhEh"
# toggleChar("This will be alternated", alternating)
# > "ThIs WiLl Be AlTeRnAtEd"

# Given a string s consisting of letters, convert each character to its opposite case that is, 
# change every lowercase letter to uppercase, and every uppercase letter to lowercase. 
# Bonus: add an "alternate" parameter that converts the whole string to AlTeRnAtE cAsE!
