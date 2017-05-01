def func1(*args):
    sum_v = 0
    for n in args:
        sum_v += n
    return sum_v

print(func1(5,4,3,2,1))
print(func1(10,9,8,7,6,5,4,3,2,1))
