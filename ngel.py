def next_greatest_left(a):
    s = []
    res = [-1] * len(a)
    
    for i in range(len(a)):
        while s and a[s[-1]] < a[i]:
            res[s.pop()] = a[i]
        s.append(i)
    
    return res