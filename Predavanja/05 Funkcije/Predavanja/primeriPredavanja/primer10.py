def faktorijel(x):
    if x == 1:
        return 1
    else:
        return x * faktorijel(x-1)

def faktorijel1(x):
    ret_val = 1
    for i in range(1,x+1):
        ret_val = ret_val*i
    return ret_val

a = faktorijel(6)
print(a)