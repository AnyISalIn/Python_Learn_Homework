def fib(n):
    fibs = []
    for i in range(0, n+1):
        if i < 2:
            fibs.append(i)
        else:
            fibs.append(fibs[-1] + fibs[-2])

    return fibs[n]

print fib(100)
