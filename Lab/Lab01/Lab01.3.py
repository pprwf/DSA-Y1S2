'''
จงเขียนฟังก์ชัน minmax(data) ที่รับค่าลิสต์ข้อมูลตัวเลข (data) และทำการคืนค่า (return) ผลลัพธ์เป็นข้อมูล tuple ความยาว 2 ข้อมูล
• ไม่อนุญาตให้ใช้ built-in function min(), max()
Ex.
• minmax([22,54,7,87,12,9,63,55,48])
• ผลลัพธ์ คือ (7, 87)
'''

def minmax(data):
    '''final lab'''
    maximum, minimum = int(data[0]), int(data[0])
    for i in data:
        maximum = int(i) if int(i) >= maximum else None
        minimum = int(i) if int(i) <= minimum else None
    return tuple([minimum, maximum])
print(minmax(input().split(",")))
