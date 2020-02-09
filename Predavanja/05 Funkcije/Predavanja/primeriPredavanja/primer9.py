def f(x):
    if x == 998:
        return x
    else:
        return f(x+1)

a = f(1000)
print(a)