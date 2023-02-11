'''Singly Linked List'''

class SinglyLinkedList:
    
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self): # ดูข้อมูลของทั้งลิสต์
        pos = self.head

        # กรณีไม่มีข้อมูลอยู่ในลิสต์
        if pos == None:
            return print("This is an empty list.")

        # ถ้าข้อมูลตัวสุดท้ายยังไม่เป็น null
        while pos != None:
            print(pos.name, end="")
            # เลื่อน pos เป็น link ตัวถัด ๆ ไป
            pos = pos.next
            print(" --> ", end="") if pos != None else print("") # ถ้า link ยังไม่เป็น null จะแสดงผล " --> " ออกมา

    def insertFront(self, data): # เพิ่มข้อมูล data ลงบนตำแหน่งแรกสุดของลิสต์
        newDat = DataNode(data)

        # กรณียังไม่มีข้อมูลอยู่ในลิสต์
        if self.head == None:
            self.head = newDat
        else:
            newDat.next = self.head
            self.head = newDat
        self.count += 1
        print("insertFront (%s) : " %data)
        self.traverse()

    def insertLast(self, data): # เพิ่มข้อมูล data ลงบนตำแหน่งท้ายสุดของลิสต์
        newDat = DataNode(data)
        print("insertLast (%s) : " %data)

        # กรณียังไม่มีข้อมูลอยู่ในลิสต์
        if self.head == None:
            self.head = newDat
        else:
            pos = self.head

            # ถ้าข้อมูลตัวสุดท้ายยังไม่เป็น null
            while pos.next != None:
                pos = pos.next
            pos.next = newDat
        self.count += 1
        self.traverse()

    def insertBefore(self, node, data): # เพิ่มข้อมูล data ลงไปในตำแหน่งก่อนหน้าข้อมูล node
        newDat, start, pos = DataNode(data), self.head, self.head.next
        print("insertBefore (%s before %s): " %(data, node))
        
        # กรณีข้อมูลตัวแรกสุดของลิสต์ = node
        if self.head.name == node:
            newDat.next, self.head = start, newDat
            self.count += 1
            self.traverse()
            return

        # ถ้าข้อมูลตัวสุดท้ายยังไม่เป็น null
        while pos != None:
            
            # ถ้าข้อมูลของโหนดที่ pos ชี้อยู่ = node
            if pos.name == node:
                newDat.next = pos
                start.next = newDat
                self.count += 1
                self.traverse()
                return
            start, pos = start.next, pos.next
        return print("Cannot insert,", node, "does not exist.")

    def delete(self, data): # ลบข้อมูล data ออกจากลิสต์
        print("delete (%s): " %data)
        start, deleting = self.head, self.head.next

        # กรณีข้อมูลตัวแรกสุดของลิสต์ = data
        if start.name == data:
            self.head = deleting
            del start
            self.count -= 1
            self.traverse()
            return

        # ถ้าข้อมูลตัวสุดท้ายยังไม่เป็น null
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
