class MyHashSet(object):
    def __init__(self, set = []):
        self.set = []
        

    def add(self, key):
        if self.contains(key): return;
        self.set.append(key)
        

    def remove(self, key):
        self.set = [el for el in self.set if el != key]
        

    def contains(self, key):
        for el in self.set:
            if el == key:
                return True
        return False;
    
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1);      # set = [1]
print(obj.set)
obj.add(2);      # set = [1, 2]
print(obj.set)
print(obj.contains(1)); # return True
print(obj.contains(3)); # return False, (not found)
obj.add(2);      # set = [1, 2]
print(obj.set)
obj.contains(2); # return True
obj.remove(2);   # set = [1]
obj.contains(2); # return False, (already removed)


# param_3 = obj.contains(key)