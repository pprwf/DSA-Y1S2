from time import time

def summation (n):
    return sum([i for i in range(1, n + 1)])

''' for those who doesn't understand use this code instead
def summation (n, add=0):
    for i in range(1, n + 1):
        add += i
    return add
'''

def summation_again (n):
    return ((n + 1) * n) / 2

def analyze_algo (n = 1):
    stime = time()
    summation(n)
    print("execution time:", time() - stime)
    stime = time()
    summation_again(n)
    print("execution time:", time() - stime)

analyze_algo(10000)
analyze_algo(10000)
