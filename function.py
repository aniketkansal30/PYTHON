def GeometricMean(a,b):
    mean=(a*b)/(a+b)
    print (mean)
def Greater(a,b):
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")
def average(a,b):
    print("average= ",(a+b)/2)
a=5
b=6
GeometricMean(a,b)
Greater(a,b)
average(a,b)

# we can change the value
average(a=10,b=20)