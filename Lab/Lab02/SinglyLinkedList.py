'''Singly Linked List'''

class SinglyLinkedList:

    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        pos = self.head
        if pos == None:
            return print("This is an empty list.")
        while pos != None:
            print(pos.name, end="")
            pos = pos.next
            print(" --> ", end="") if pos != None else print("")

    def insertFront(self, data):
        newDat = DataNode(data)
        if self.head == None:
            self.head = newDat
        else:
            newDat.next = self.head
            self.head = newDat
        self.count += 1
        print("insertFront (%s) : " %data)
        self.traverse()

    def insertLast(self, data):
        newDat = DataNode(data)
        print("insertLast (%s) : " %data)
        if self.head == None:
            self.head = newDat
        else:
            pos = self.head
            while pos.next != None:
                pos = pos.next
            pos.next = newDat
        self.count += 1
        self.traverse()

    def insertBefore(self, node, data):
        newDat, start, pos = DataNode(data), self.head, self.head.next
        print("insertBefore (%s before %s) : " %(data, node))
        if self.head.name == node:
            newDat.next, self.head = start, newDat
            self.count += 1
            self.traverse()
            return
        while pos != None:
            if pos.name == node:
                newDat.next = pos
                start.next = newDat
                self.count += 1
                self.traverse()
                return
            start, pos = start.next, pos.next
        return print("Cannot insert,", node, "does not exist.")

    def delete(self, data):
        print("delete (%s): " %data)
        start, deleting = self.head, self.head.next
        if start.name == data:
            self.head = deleting
            del start
            self.count -= 1
            self.traverse()
            return
        while deleting != None:
            if deleting.name == data:
                start.next = deleting.next
                del deleting
                self.count -= 1
                self.traverse()
                return
            start, deleting = start.next, deleting.next
        return print("Cannot delete,", data, "does not exist.")

class DataNode:
    def __init__(self, name=""):
        self.name = name
        self.next = None

dataSet = SinglyLinkedList()
dataSet.head = DataNode("FirstData")
dataSet.count += 1
print("----------")
print("Traverse : \n", end="")
dataSet.traverse()
print("----------")
dataSet.insertFront("Front")
print("----------")
dataSet.insertLast("Last")
print("----------")
dataSet.insertBefore("Last", "newLast")
print("----------")
dataSet.delete("Last")
print("----------")
