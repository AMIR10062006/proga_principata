def prime(mylst=[],*args):
    for i in mylst:
        if isprime(i):
            print(i)

lst = []
n = int(input())
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
prime(lst,n)
