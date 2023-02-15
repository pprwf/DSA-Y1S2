'''Infix to Postfix'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def push(self, data):
        print("Push \"%s\" : " %data, end="")
        self.data.append(data)
        self.printStack()

    def pop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
        else:
            value = self.data[-1]
            print("Pop  \"%s\" : " %value, end="")
            self.data.pop()
            self.printStack()
            return value

    def printStack(self):
        print(self.data)

def infixToPostfix(expression, postfix=""):
    operatorStack = ArrayStack()
    print("----------")
    for i in expression:
        if i.isalpha():
            postfix += i
        elif i in "+-*/":
            if operatorStack.is_empty():
                operatorStack.push(i)
            else:
                if i in "+-":
                    while not operatorStack.is_empty():
                        postfix += operatorStack.pop()
                operatorStack.push(i)
    while not operatorStack.is_empty():
        postfix += operatorStack.pop()
    return postfix

exp = "A+B*C-D/E"
postfix = infixToPostfix(exp)
print("Postfix of", exp, "is", postfix)
print("----------")
