class ProbHash:
    
    def __init__(self, position):
        self.hashtable = position * [None]
        self.size = position

    def hash(self, key):
        return key % self.size

    def rehash(self, hkey):
        result = self.hash(hkey)
        while self.hashtable[result] != None:
            result += 1
        return result

    def insertData(self, student):
        result = self.rehash(student.id)
        print("Insert", student.id, "at index", result)
        self.hashtable[result] = student

    def searchData(self, std_id):
        for key in self.hashtable:
            if key != None and key.id == std_id:
                print("Found", std_id, "at index", self.hashtable.index(key))
                return self.hashtable[self.hashtable.index(key)]
        print(std_id, "does not exist.")

class Student:

    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getGPA(self):
        return self.gpa

    def printDetail(self):
        print("ID:", self.id, "\nName:", self.name, "\nGPA:", self.gpa)

s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)
myHash = ProbHash(20)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)
print("-------------------------")
myHash.searchData(65070077).printDetail()
print("-------------------------")
myHash.searchData(65070021).printDetail()
print("-------------------------")
myHash.searchData(65070042).printDetail()
print("-------------------------")
myHash.searchData(65070032)
print("-------------------------")
