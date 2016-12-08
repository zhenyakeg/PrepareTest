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
class SmileChecker:
    def __init__(self):
        self.Left = [':-(', ':-[', ':-{', ':-<']
        self.Right = [':-)', ':-]', ':-}', ':->']
        self.pair = dict(zip(self.Left, self.Right))
        self.list = []
        self.stack = LinkedList()
    def append_smile(self,data):
        self.list.append(data)
    def check_correct(self):
        for brace in self.list:
            if brace in self.Left:
                self.stack.push_front(brace)
            elif brace in self.Right:
                if self.stack.empty():
                    return False
                if self.pair[self.stack.pop_front()] != brace:
                    return False
        return self.stack.empty()
