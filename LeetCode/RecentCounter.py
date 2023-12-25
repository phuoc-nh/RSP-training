from queue import Queue

class RecentCounter(object):

    def __init__(self):
        self.q = Queue()

    def ping(self, t):
        self.q.put(t)
        while self.q.queue[0] < t - 3000:
            self.q.get()
        
        # print('self.q.qsize()', self.q.qsize())
        return self.q.qsize()
    
    
rc = RecentCounter()

rc.ping(1)
rc.ping(100)
rc.ping(3001)
rc.ping(3002)