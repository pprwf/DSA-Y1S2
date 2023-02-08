'''
จงเขียนฟังก์ชัน is_even(k) ที่รับค่าตัวเลขจำนวนเต็ม 1 ค่า (k)และทำการคืนค่า (return) ผลลัพธ์เป็นค่า True หรือ False
• คืนค่า True ก็ต่อเมื่อ k เป็นเลขคู่
• ไม่เช่นนั้น ให้คืนค่า False
• ไม่อนุญาตให้ใช้โอเปอเรเตอร์สำหรับการคูณ การ mod หรือ การหาร
ตัวอย่าง
• is_even(22)
• ผลลัพธ์ คือ True
'''

def is_even(k_num):
    '''fuq pep8'''
    while k_num > 0: k_num -= 2
    return True if k_num == 0 else False
print(is_even(int(input())))
