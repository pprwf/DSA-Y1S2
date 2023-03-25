from time import time
from random import randint

def isintersect (a, b, c):
    for i in a:
        for j in b:
            if i == j:
                for k in c:
                    if i == k:
                        return True
    return False

def isintersect_again (a, b, c):
    for i in a:
        for j in b:
            for k in c:
                if i == j and i == k:
                    return True
    return False

def random_List (n):
    lis = []
    while len(lis) != n:
        num = randint(0, n*100)
        if num not in lis:
            lis.append(num)
    return lis

def analyze_algo (n):
    num1 = random_List(n)
    num2 = random_List(n)
    num3 = random_List(n)
    
    # O ** 2
    stime = time()
    print(isintersect(num1, num2, num3))
    print("execution time:", time() - stime)
    
    # O ** 3
    stime = time()
    print(isintersect_again(num1, num2, num3))
    print("execution time:", time() - stime)

analyze_algo(10000)
