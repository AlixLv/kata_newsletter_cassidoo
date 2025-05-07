# Function to create combinations 
# without itertools

# générer toutes les combinaisons possibles de lonugeur n, à partir d'une liste lst.
def n_length_combo(lst, n):
    # cas de base permettant d'arrêter la récursivité
    if n == 0:
        return [[]]
    
    # contiendra toutes les combinaisons 
    l =[]
    for i in range(0, len(lst)):
        # pour chaque élément actuel m
        m = lst[i]
        print("🌼 m: ", m)
        # création d'une sous-liste contenant tous les éléments qui suivent m
        remLst = lst[i + 1:]
        print("🌸 remLst: ", remLst)
        
        # appel récursif de la fonction sur la sous-liste, pour obtenir toutes les combinaisons de longueur n-1 
        # appel exécuté complètement avant que la boucle for p in remianlst_combo ne commence! 
        remainlst_combo = n_length_combo(remLst, n-1)
        
        for p in remainlst_combo:
            print("🍀 remainlst_combo: ", remainlst_combo)
            print("🍎 p: ", p)
            l.append([m, *p])
            print("🍊 l: ", l)
           
    return l
 
# Driver code
if __name__=="__main__":
    arr ="abc"
    print(n_length_combo([x for x in arr], 2))