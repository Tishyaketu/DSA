class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def transfer(self, instack, outstack):
      if not outstack:
        while(instack):
          self.outstack.append(instack.pop())
      return outstack
    def push(self, x: int) -> None:
        self.instack.append(x)

    def pop(self) -> int:
        self.transfer(self.instack,self.outstack)
        return self.outstack.pop()

    def peek(self) -> int:
        self.transfer(self.instack,self.outstack)
        return self.outstack[-1]

    def empty(self) -> bool:
        return (not self.instack) and (not self.outstack)        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()