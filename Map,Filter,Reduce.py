def cube(x):
    return x*x*x
l=[1,2,3,4,5]
# newl=[]
# for item in l:
#     newl.append(cube(item))

# MAP
newl=list(map(cube,l))
print (newl)
# FILTER
def filter_fun(a):
    return a>2
newL=list(filter(filter_fun,l))
print(newL)
# REDUCE
from functools import reduce
sum=reduce(lambda x,y:x+y,l)
print(sum)