'''
จงเขียนฟังก์ชัน is_multiple(n,m) ที่รับค่าตัวเลขจำนวนเต็ม 2 ค่า (n และ m) และทำการคืนค่า (return) ผลลัพธ์เป็นค่า True หรือ False
• คืนค่า True ก็ต่อเมื่อ n = mi โดยที่ i เป็นเลขจำนวนเต็ม
• ไม่เช่นนั้น ให้คืนค่า False
Ex.
• is_multiple(10, 3)
• ผลลัพธ์ คือ False
'''

def is_multiple(n_num, m_num):
    '''does it need to follow PEP-8 in order to finish this lab test?'''
    return True if n_num == m_num else False
print(is_multiple(int(input()), int(input())))
