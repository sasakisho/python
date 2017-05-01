def fanc(n=5):
    if n == 0:
        return 1
    else:
        return n * fanc(n-1)

print(fanc())
