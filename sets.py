a={1,2,3,4,5}
b={6,7,8,9,10}
print(a.union(b))
a={1,2,3,4,5}
b={4,5,6,7,8,9}
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.difference(b))
print(a.isdisjoint(b)) #no common value 