class MinStack:

    def __init__(self):
        self.MinStack=[]
        self.Stack = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        if not self.Stack or self.getMin()>=val:
            self.Stack.append(val)

    def pop(self) -> None:
        if not self.MinStack:
            return -1
        temp = self.MinStack.pop()
        if temp == self.getMin():
            self.Stack.pop()
        
        return temp

    def top(self) -> int:
        if not self.MinStack:
            return -1
        return self.MinStack[-1]

    def getMin(self) -> int:
        if not self.Stack:
            return -1
        return self.Stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()