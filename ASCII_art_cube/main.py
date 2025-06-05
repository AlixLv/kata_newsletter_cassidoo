def draw_cube(n:int)->str:
    if n <= 0:
        return ""
    
    width = n * 2
    offset = int(n/2)
    print(offset)

    plain_line="-"*width
    empty_line=" "*width    
    
    #top ligne
    print(" " * (offset+1) + "+" + plain_line + "+")  

    #lignes face du dessus
    for i in range(int(n/2)):
        print(" " * offset + "/" + empty_line + "/" + " "* i + "|") 
        offset-=1 
        if i == int(n/2)-1:
            print("+" + plain_line + "+" + " " * (i+1) + "|")

    # lignes face avant
    for i in range(n):
        if i < (int(n/2)-1):
            print("|" + empty_line + "|" + " " * int(n/2) + "|")
        elif i == (int(n/2)-1):
            print("|" + empty_line + "|" + " " * int(n/2) + "+")
        else:
            print("|" + empty_line + "|" + " " * int(n-i-1) + "/")
                
    print(f"+{plain_line}+")    
        
              
    
if __name__ == "__main__":
    draw_cube(4)    
    