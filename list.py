l=[2,86,58,74,44,40]
l.reverse()
print(l)
l.append(7)
print(l)
l.sort() #asscending
print(l)
l.sort(reverse=True) #descending
print(l)
print(l.index(2))
print(l.count(2))
l[0]=0
print(l)
l.insert(1,55)
print(l)