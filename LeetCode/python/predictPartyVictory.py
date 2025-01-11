from queue import Queue

def predictPartyVictory(senate):
    direQ = Queue()
    radiantQ = Queue()
    
    for i in range(len(senate)):
        if senate[i] == "D":
            direQ.put(i)
        else:
            radiantQ.put(i)
            
    while not direQ.empty() and not radiantQ.empty():
        d = direQ.get()
        r = radiantQ.get()
        print(d, r)
        if d < r:
            direQ.put(d + len(senate))
        else:
            radiantQ.put(r + len(senate))
            

    return "Dire" if direQ.qsize() else "Radiant"
    
senate = "RDD"
print(predictPartyVictory(senate))