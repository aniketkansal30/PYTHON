f=open('file.txt','r')
r=f.read()
print(r)
f.seek(9) #iska mtlb hota h ki jo ab output aayega voh 9 index k baad s start hoga
print(f.tell()) #yeh bta de kitne index k baad start h
data=f.read(6)
print(data)

f=open('file.txt','r+')
f.truncate(3)
print(f)
