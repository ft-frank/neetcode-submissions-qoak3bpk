class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif self.minstack[-1] > val:
            self.minstack.append(val)
        else:
            self.minstack.append(self.getMin())

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minstack:
            self.minstack.pop()


    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
        return top

    def getMin(self) -> int:
        if self.minstack:
            minimum =  self.minstack[-1]
        return minimum
