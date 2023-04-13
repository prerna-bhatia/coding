def next_smallest_element_left(a):
    n = len(a)
    res = [-1] * n
    s = []
    for i in range(n):
        while s and a[i] < a[s[-1]]:
            res[s.pop()] = a[i]
        s.append(i)
    return res