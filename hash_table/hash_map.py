class MyHashMap(object):

    def __init__(self, map = []):
        self.map = []
        

    def put(self, key, value):
        for el in self.map:
            if el[0] == key:
                el[1] = value
                return;
        self.map.append([key, value])
        
        

    def get(self, key):
        for el in self.map:
            if el[0] == key:
                return el[1]
        return -1;

    def remove(self, key):
        self.map = [val for val in self.map if key != val[0]]        



# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1); # The map is now [[1,1]]
obj.put(2, 2); # The map is now [[1,1], [2,2]]
obj.get(1);    # return 1, The map is now [[1,1], [2,2]]
obj.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
obj.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
# obj.get(2);    # return 1, The map is now [[1,1], [2,1]]
print(obj.get(2))

obj.remove(2); # remove the mapping for 2, The map is now [[1,1]]
obj.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]