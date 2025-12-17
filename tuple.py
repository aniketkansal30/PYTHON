fruits=("apple","mango","banana")
temp=list(fruits) #phele tuple ko list m change kra phr change kr diye
temp.append("cheeku") #add
temp.pop(0) #remove
temp[1]="pineapple" #change
fruits=tuple(temp)
print(fruits)

# index method
# tuple.index(element,start,end)
tup=(0,1,2,3,4,5,2,3,5,4,3)
res=tup.index(3,0,6) #toh jo bhi sbse pheli bri index p milega voh print hojayegaa
print(res)