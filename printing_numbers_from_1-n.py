def f(num):
    if num==0:
        return
    else:
        f(num-1)
    print(num,end=" ")
    return