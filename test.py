def callfunc(n):
    if n==0:
        return 1
    else:
        power = callfunc(n-1)
        return power * 2

print(callfunc(4))