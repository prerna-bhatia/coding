def next_smallest_element_right(a):
    s = []
    res = [-1] * len(a)
    for i in range(len(a)-1, -1, -1):
        while s and a[i] < s[-1]:
            s.pop()
        if s:
            res[i] = s[-1]
        s.append(a[i])
    return res