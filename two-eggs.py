N = 100
a = [None] * (N+1)
b = [None] * (N+1)

a[1] = 1
a[2] = 2
a[3] = 2
a[4] = 3

for i in range(5, N+1):
    # a[i] = min_j max(j, 1 + a[i-j])
    min_max = i
    min_j = None
    # for j in range(1, i):
    # Reverse search to produce more understandable solution
    for j in range(i-1, 0, -1):
        t = max(j, 1 + a[i-j])
        if t < min_max:
            min_max = t
            min_j = j
    assert min_j
    a[i] = min_max
    b[i] = min_j

print "Best worst-case for", N, "floors:", a[N]
i = N
j = 0
while b[i]:
    j += b[i]
    i -= b[i]
    print j
