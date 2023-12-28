from queue import Queue

def predictPartyVictory(senate):
    direQ = Queue()
    radiantQ = Queue()

    for i in range(len(senate)):
        if senate[i] == 'R':
            radiantQ.put(i)
        else:
            direQ.put(i)      

    while direQ.qsize() and radiantQ.qsize():
        dire = direQ.get()
        radiant = radiantQ.get()
        
        if dire < radiant: # remove radiant, add dire with index n + cur
            direQ.put(dire + len(senate))
        else:
            radiantQ.put(radiant + len(senate))
        
    return 'Radiant' if radiantQ.qsize() else 'Dire'
    
senate = "RDD"
print(predictPartyVictory(senate))