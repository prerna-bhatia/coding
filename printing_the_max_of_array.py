def Max(A, n):
 
    # if n = 0 means whole array
    # has been traversed
    if (n == 1):
        return A[0]
    return max(A[n - 1], Max(A, n - 1))
