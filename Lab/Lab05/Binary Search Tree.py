'''BST'''

class BST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, data):
        newBST = BSTNode(data)
        if self.root == None:
            self.root = newBST
        else:
            prev, this = None, self.root
            while this != None:
                if data < this.data:
                    prev, this = this, this.left
                elif data > this.data:
                    prev, this = this, this.right
            if prev.data > data:
                prev.left = newBST
            elif prev.data < data:
                prev.right = newBST

    def delete(self, data):
        prev, this = None, self.root
        if self.root.data == data and this.left == None and this.right == None:
            self.root = None
            del this
            return data
        while this != None:
            if data > this.data:
                prev, this = this, this.right
            elif data < this.data:
                prev, this = this, this.left
            elif data == this.data:
                if this.left == None and this.right == None:
                    prev.left = (None if this.data < prev.data else prev.left)
                    prev.right = (None if this.data > prev.data else prev.right)
                elif this.left != None and this.right != None:
                    prev, this, pointer = this, this.left, this
                    if this.right == None:
                        prev.data, prev.left = this.data, this.left
                        if this.left != None:
                            prev.left = this.left
                        del this
                        return data
                    while this.right != None:
                        pointer, this = this, this.right
                    prev.data, pointer.right = this.data, this.right
                else:
                    if self.root.data == data:
                        self.root = (this.left if this.left != None else this.right)
                        del this
                        return data
                    prev.left = (this.left if this.left != None else this.right) if data < prev.data else None
                    prev.right = (this.left if this.left != None else this.right) if data > prev.data else None
                del this
                return data
        return None

    def preorder(self, root):
        if root == self.root and self.root != None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        elif root != None:
            print("-->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        this = self.root
        while this.left != None:
            this = this.left
        if root == this:
            print(root.data, end=" ")
            self.inorder(root.right)
        elif root != None:
            self.inorder(root.left)
            print("-->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        this = self.root
        while this.left != None:
            this = this.left
        while this.right != None:
            this = this.right
        if root == this:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")
        elif root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("-->", root.data, end=" ")

    def traverse(self):
        print("Traverse (Preorder):\n", end="")
        self.preorder(self.root)
        print("\nTraverse (Inorder) :\n", end="")
        self.inorder(self.root)
        print("\nTraverse (Postorder) :\n", end="")
        self.postorder(self.root)
        print()

    def findMin(self):
        pointer = self.root
        while pointer.left != None:
            pointer = pointer.left
        return pointer.data

    def findMax(self):
        pointer = self.root
        while pointer.right != None:
            pointer = pointer.right
        return pointer.data

class BSTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

myBST = BST()
myBST.insert(14)
myBST.insert(23)
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
print("----------\n")
myBST.traverse()
print("\n----------\n")
myBST.delete(14)
myBST.traverse()
print("\nMin:", myBST.findMin())
print("Max:", myBST.findMax())
print("----------")
