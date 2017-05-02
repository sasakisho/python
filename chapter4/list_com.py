# data = [i*2 for i in range(1,6)]
# print(data)
#
# data = [i for i in range(1,11) if i%2 == 1]
# print(data)
# 
# base = [1,2,3]
# result = [(x,y) for x in base for y in base if x!=y]
# print(result)

res = [
    "Fizz Buzz" if i % 15==0 else "Fizz"
                if i % 3==0 else "Buzz"
                if i % 5==0 else str(i)
    for i in range(1,21)
]
print("\n".join(res))
