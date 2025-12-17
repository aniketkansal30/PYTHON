a="aniket"
print(len(a))
print(a.upper())
print(a.lower())
b="!!aniket!!"
print(b.rstrip("!")) #naam k aage vale ! htt jaayengee
print(a.replace("aniket","Aniket"))
fruits="mango apple banana"
print(fruits.split(" ")) #list m convert
print(a.capitalize())
print(a.center(20)) # center m laa dega text ko jitna spacing krana chayoge
print(b.endswith("!!"))
print(fruits.find("apple"))
# isalnum() returns true only if A-Z,a-z,0-9 otherwise false
c="ANIKET"
print(c.isalnum())
d="aniketkansal"
print(d.isalnum())
e="8126700718"
print(e.isalnum())
f="Aniket8126700718"
print(f.isalnum())
# isalpha() returns true only if A-Z,a-z otherwise false
print(a.isalpha())
# istitle() true jb dega agr hrr word k 1st letter capital hoga
g="World Health Organization"
print(g.istitle())
# swapcase() saare uppercase ko lowercase m convert krdega and vice versa
# title() saare words ka 1st letter capital krdega
