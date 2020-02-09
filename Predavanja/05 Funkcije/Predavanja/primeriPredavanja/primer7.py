l = [1,2,3]

def f(x):
    x[0] = 100
    print('x u funkciji: ',x)

f(l)
print('l van funkcije: ',l)