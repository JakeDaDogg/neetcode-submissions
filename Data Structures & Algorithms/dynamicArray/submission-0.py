class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.length = 0
        self.array = [0]*capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        return

    def pushback(self, n: int) -> None:
        if self.length == self.cap:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        ele = self.array[self.length]
        self.array[self.length] = 0
        return ele

    def resize(self) -> None:
        self.cap = self.cap*2
        newarr = [0]*self.cap
        newarr[:self.length] = self.array
        self.array = newarr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.cap
