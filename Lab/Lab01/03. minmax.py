'''Lab 1.3 Finding max & min values'''

def minmax(data):
    '''final lab'''
    maximum, minimum = int(data[0]), int(data[0])
    for i in data:
        maximum = int(i) if int(i) >= maximum else None
        minimum = int(i) if int(i) <= minimum else None
    return tuple([minimum, maximum])
print(minmax(input().split(",")))
