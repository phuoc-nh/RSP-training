from collections import Counter
def isNStraightHand(hand, groupSize):
    counter = Counter(hand)
    
    keys = list(counter.keys())
    keys.sort()
    print(keys)
    for card in keys:
        print(card)
        count = counter[card]
        for i in range(count):
            for j in range(1, groupSize):
                if card + j in counter and counter[card + j] > 0:
                    counter[card + j] = counter[card + j] - 1
                else:
                    return False
                
    
    return True
    
hand = [2, 1]
groupSize = 2

print(isNStraightHand(hand, groupSize))