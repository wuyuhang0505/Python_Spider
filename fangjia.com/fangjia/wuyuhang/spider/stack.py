
class stack:
    items_tmp=[]
    def __init__(self,s):
        self.items_tmp=s
        self.items =s
    def push(self, item):
        #move the repeat item
        if item not in self.items_tmp:
            self.items.append(item)
        return None

    def pop(self):
        return self.items.pop()

    def clear(self):
        del self.items[:]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[self.size()-1]
    