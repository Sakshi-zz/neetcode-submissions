class MinStack:

    def __init__(self):
        self.stack = []       # main stack
        self.min_stack = []   # tracks minimum at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new minimum (or val itself if stack was empty)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()   # keep both in sync

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]