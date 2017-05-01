points=[88,76,67,43,79,80,91]

sum_v = 0
#for i in points:
    #sum_v += i
    #print(i,"点を足して合計は",sum_v)

sum_v=sum(points)

ave_v = sum_v/len(points)
print("平均点は",round(ave_v,2),"点")
