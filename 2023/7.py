from aocd import get_data, submit

day = 7
data = get_data(day=day, year=2023).splitlines()

card_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14
}

### PART 1 ###
# def is_stronger(hand1, hand2):
#     def get_hand_score(hand):
#         cards = [0 for _ in range(15)]
#         for c in hand:
#             cards[card_values[c]] += 1

#         if set(cards) == {0,5}:
#             return 100
#         if set(cards) == {0,1,4}:
#             return 99
#         if set(cards) == {0,2,3}:
#             return 98
#         if set(cards) == {0,1,3}:
#             return 97
#         if len(list(filter(lambda x: x == 2, cards))) == 2:
#             return 96
#         if set(cards) == {0, 1, 2}:
#             return 95

#         return 0

#     score1 = get_hand_score(hand1)
#     score2 = get_hand_score(hand2)

#     if score1 > score2:
#         return True
    
#     if score1 < score2:
#         return False

#     return [card_values[c] for c in hand1] > [card_values[c] for c in hand2]


### PART 2 ###
def is_stronger(hand1, hand2):
    def get_hand_score(hand):
        cards = [0 for _ in range(15)]
        for c in hand:
            cards[card_values[c]] += 1

        if set(cards) == {0,5}:
            return 100
        if set(cards) == {0,1,4}:
            return 99
        if set(cards) == {0,2,3}:
            return 98
        if set(cards) == {0,1,3}:
            return 97
        if len(list(filter(lambda x: x == 2, cards))) == 2:
            return 96
        if set(cards) == {0, 1, 2}:
            return 95

        return 0

    score1 = 0
    if "J" in hand1:
        score1 = max([get_hand_score(hand1.replace("J", x)) for x in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]])
    else:
        score1 = get_hand_score(hand1)

    score2 = 0
    if "J" in hand2:
        score2 = max([get_hand_score(hand2.replace("J", x)) for x in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]])
    else:
        score2 = get_hand_score(hand2)

    if score1 > score2:
        return True
    
    if score1 < score2:
        return False

    return [card_values[c] for c in hand1] > [card_values[c] for c in hand2]



hands = []
for l in data:
    hand = l.split(" ")
    i = len(hands) - 1
    while i >= 0:
        if is_stronger(hand[0], hands[i][0]):
            break
        i -= 1
    
    hands = [*hands[:i+1], hand, *hands[i+1:]]

result = 0
for i in range(len(hands)):
    result += int(hands[i][1]) * (i+1)

submit(result, day=day, year=2023)