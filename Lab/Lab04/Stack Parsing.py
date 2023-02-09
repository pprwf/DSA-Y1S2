'''Stack'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return True if self.data == [] else False

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
        else:
            value = self.data[-1]
            self.data.pop()
            return value

    def printStack(self):
        print(self.data)

    def is_parentheses_matching(self, expression):
        for i in expression:
            if i == "(":
                self.push(i)
            elif i == ")":
                self.pop()
        if self.data != []:
            print("Parentheses in", expression, "are unmatched")
        return self.is_empty()

parsingStack = ArrayStack()
str = "(((A - B) * C)"
result = parsingStack.is_parentheses_matching(str)
print(result)
