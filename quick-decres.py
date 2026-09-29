def quickDecres (A, p, r):
    if p < r:
        q = partDecres (A, p, r)
        quickDecres(A, p, q-1)
        quickDecres(A, q+1, r)

def partDecres (A, p, r):
    x = A[r]
    i = p-1
    for j in range (p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

A = [10, 5, 8, 1, 7]
print(A)
quickDecres(A, 0, len(A)-1)
print(A)