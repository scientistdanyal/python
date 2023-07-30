def fabonacci(n):
    mylist = [0,1]
    if n in mylist:
        return n
    return (fabonacci(n-2)+fabonacci(n-1))

for i in range(10):
    print(fabonacci(i))