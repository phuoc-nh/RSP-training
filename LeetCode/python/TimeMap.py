class TimeMap:

    def __init__(self):
        self.list = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.list:
            self.list[key] = []
            self.list[key].append((value, timestamp))
        else:
            self.list[key].append((value, timestamp))
            

    def get(self, key: str, timestamp: int) -> str:
        # print('>>',self.list[key])
        if key not in self.list:
            return ''
        
        curList = self.list[key]
        # print('curl', curList)
        l = 0
        r = len(curList) - 1
        res = ''
        while l <= r:
            m = (l + r) // 2
            # print('m', m)
            if curList[m][1] <= timestamp:
                res = curList[m][0]
                l = m + 1
            else:
                r -= 1
        # print('res', res)
        return res
                
        
        
        # we want timestamp in map closet to timestamp
            


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
obj.get("foo", 1)
obj.get("foo", 3)         # return "bar  since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# param_2 = obj.get(key,timestamp)

obj.set("foo", "bar2", 4) # store the key "foo" and value "bar2" along with timestamp = 4.
obj.get("foo", 4)         # return "bar2"
obj.get("foo", 5)         # return "bar2"

print(obj.list)