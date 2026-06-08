def max_solitaire_moves_01(deck:list) -> int:
    """
    You have a "mini" version of solitaire in front of you. 
    There is a row of cards, where each card has a rank from 1 to 13 and a color of "red" or "black". 
    In one move, you may place a card onto another card immediately to its left if its rank is exactly one less and its color is opposite, then remove the moved card from its original position. 
    Return the maximum number of valid moves you can make by repeatedly scanning left to right.
    """
    moves = 0
    
    for index, card in enumerate(deck):
        # condition d'arrêt pour ne pas sortir du deck
        if index < len(deck) -1:
            actuelle = cards[index]
            suivante = cards[index + 1]
            if actuelle['rank'] - suivante['rank'] == 1 and actuelle['color'] !=  suivante['color']:
                print(f"🌼 carte n°{suivante['rank']}, couleur {suivante['color']} peut monter sur carte n° {actuelle['rank']}, couleur {actuelle['color']}")
                moves += 1
            else:
                print(f"🌸 carte n°{suivante['rank']}, couleur {suivante['color']} ne monte pas sur carte n° {actuelle['rank']}, couleur {actuelle['color']}")

    return moves


def max_solitaire_moves_02(deck:list) -> int:
    moves = 0 
    
    for index in range(len(deck) -1):
        actuelle = deck[index]
        suivante = deck[index + 1]
        if actuelle['rank'] - suivante['rank'] == 1 and actuelle['color'] !=  suivante['color']:
            print(f"🌼 carte n°{suivante['rank']}, couleur {suivante['color']} peut monter sur carte n° {actuelle['rank']}, couleur {actuelle['color']}")
            moves += 1
        else:
            print(f"🌸 carte n°{suivante['rank']}, couleur {suivante['color']} ne monte pas sur carte n° {actuelle['rank']}, couleur {actuelle['color']}")

    return moves


def max_solitaire_moves_03(deck:list) -> int:
    moves = 0 
    
    for actuelle, suivante in zip(deck, deck[1:]):
        if actuelle['rank'] - suivante['rank'] == 1 and actuelle['color'] !=  suivante['color']:
            print(f"🌼 carte n°{suivante['rank']}, couleur {suivante['color']} peut monter sur carte n° {actuelle['rank']}, couleur {actuelle['color']}")
            moves += 1
        else:
            print(f"🌸 carte n°{suivante['rank']}, couleur {suivante['color']} ne monte pas sur carte n° {actuelle['rank']}, couleur {actuelle['color']}")

    return moves   


if __name__ == "__main__":
    cards = [
    { "rank": 7, "color": "black" },
    { "rank": 6, "color": "red" },
    { "rank": 5, "color": "black" },
    { "rank": 9, "color": "red" }
    ]
    
    moves = max_solitaire_moves_01(cards) 
    print(f"🌈 nombre de mouvements possibles: {moves}")
    print("------------------")

    cards2 = [
    { "rank": 8, "color": "black" },
    { "rank": 7, "color": "red" },
    { "rank": 6, "color": "red" },
    { "rank": 5, "color": "black" }
    ]
    moves2 = max_solitaire_moves_02(cards2)
    print(f"🌈 nombre de mouvements possibles: {moves2}")
    print("------------------")

    cards3 = [
    { "rank": 3, "color": "black" },
    { "rank": 2, "color": "red" },
    { "rank": 6, "color": "red" },
    { "rank": 7, "color": "black" }
    ]
    moves3 = max_solitaire_moves_03(cards3)
    print(f"🌈 nombre de mouvements possibles: {moves3}")

# > maxSolitaireMoves(cards)
# > 2 // 6 onto 7, 5 onto 6

# > maxSolitaireMoves(cards2)
# > 2 // 7 onto 8, 5 onto 6   