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

    def stackTop(self):
        return None if self.data == [] else self.data[-1]

    def printStack(self):
        print(self.data)

def infixToPostfix(expression, postfix=""):
    operatorStack = ArrayStack()
    print("----------")
    for letter in expression:
        print("Letter :", letter)
        if letter.isalpha():
            postfix += letter
        elif letter in "+-*/":
            if not operatorStack.is_empty():
                while not operatorStack.is_empty() and (operatorStack.stackTop() in "*/" or letter in "+-"):
                    postfix += operatorStack.pop()
            operatorStack.push(letter)
        print("Postfix :", postfix)
        print("----------")
    while not operatorStack.is_empty():
        postfix += operatorStack.pop()
        print("Postfix :", postfix)
        print("----------")
    return postfix

exp = "A+B*C-D/E"
postfix = infixToPostfix(exp)
print("Postfix of", exp, "is", postfix)
print("----------")
