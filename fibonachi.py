def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonachi(n-1) + fibonachi(n-2)

#print(fibonachi(20))

def fibonachi(n):
    a = 0
    b = 1
    for i in range(n):
        while a < n:
            print(a)
            a,b = b, a+b
    return a

print (fibonachi(10))
