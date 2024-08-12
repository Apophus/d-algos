class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key, value, timestamp):
        if key not in self.map.keys():
            self.map[key] = [[value, timestamp]]
        else:
            self.map[key].append([value, timestamp])
            
    def get(self, key, timestamp):
        
        values = self.map.get(key,[])
        left, right = 0, len(values) -1
        res = ''
        while left <= right:
            mid = (left+right)//2
            if timestamp >= values[mid][1]:
                res = values[mid][0]
                left = mid +1
            else:
                right = mid - 1
                
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)