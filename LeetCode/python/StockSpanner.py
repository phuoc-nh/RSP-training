class StockSpanner:

    def __init__(self):
        self.span = []

    def next(self, price: int) -> int:
        
        if len(self.span) == 0:
            self.span.append((price, 1)) # price and span
            return 1
        
        
        if price < self.span[-1][0]:
            self.span.append((price, 1)) # price and span
            return 1
        
        # price >= self.span[-1][0] now
        
        span = 1
        
        while len(self.span) > 0 and price >= self.span[-1][0]:
            span += self.span[-1][1]
            self.span.pop()
            
        self.span.append((price, span))
        
        return span
        
        
        
# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_1 = obj.next(80)
param_1 = obj.next(60)
param_1 = obj.next(70)
param_1 = obj.next(60)
param_1 = obj.next(75)
param_1 = obj.next(85)