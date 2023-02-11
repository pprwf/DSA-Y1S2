''''''

def is_even(k_num):
    '''fuq pep8'''
    while k_num > 0: k_num -= 2
    return True if k_num == 0 else False
print(is_even(int(input())))
