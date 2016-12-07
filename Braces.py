class LinkedList:
    def __init__(self):
        self._begin = None
    def push_front(self, data):
        p = self._begin
        self._begin = [data, p]
    def pop_front(self):
        if self._begin == None:
            raise IndexError
        data = self._begin[0]
        self._begin = self._begin[1]
        return data
    def empty(self):
        return not self._begin
class AnalyseBraces:
    def __init__(self, L, R):
        self.Left = L
        self.Right = R
        self.pair = dict(zip(self.Left, self.Right))
        self.stack = LinkedList()
    def checking(self, s):
        for brace in s:
            if brace in self.Left:
                self.stack.push_front(brace)
            elif brace in self.Right:
                if self.stack.empty():
                    return False
                if self.pair[self.stack.pop_front()] != brace:
                    return False
        return self.stack.empty()

Checker = AnalyseBraces(['(','[','{'],[')',']','}'])
print(Checker.checking(input()))