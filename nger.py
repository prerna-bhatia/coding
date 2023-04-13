def next_greatest_element_right(arr):
    s = []
    res = [-1] * len(arr)
    for i in range(len(arr)):
        while s and arr[s[-1]] < arr[i]:
            res[s[-1]] = arr[i]
            s.pop()
        s.append(i)
    return res