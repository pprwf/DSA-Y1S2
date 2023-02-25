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
        if self.root == data:
            return this.data
        while this != None:
            if data > this.data:
                prev, this = this, this.right
            elif data < this.data:
                prev, this = this, this.left
        return None

    def preorder(self, root):
        if root == self.root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        elif root != None:
            print("-->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print("-->", root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root != None:
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
# myBST.insert(23)
# myBST.insert(7)
# myBST.insert(10)
# myBST.insert(33)
# print("----------")
# myBST.traverse()
# print("\n----------")
myBST.delete(14)
myBST.traverse()
print("Min:", myBST.findMin())
print("Max:", myBST.findMax())
