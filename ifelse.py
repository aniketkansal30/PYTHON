# if else 

# a=int(input("Enter your age: "))
# if(a>=18):
#     print("You can drive")
# else:
#     print("You can't drive")

# else if

# a=int(input("Enter a no.: "))
# if(a<0):
#     print("Negative")
# elif(a==0):
#     print("Null")
# else:
#     print("Positive")

# nested ifelse

# a=int(input("Enter a no.: "))
# if(a<0):
#     print("Negative")
# elif(a>0):
#     if(a<10):
#         print("1-10")
#     elif(a>10 and a<=20):
#         print("11-20")
#     else:
#         print(">20")
# else:
#     print("=0")

# practice
time=int(input("Enter the current hour(0-23): "))
if(time>=5 and time<12):
    print("Good Morning")
elif(time>=12 and time<17):
    print("Good Afternoon")
elif(time>=17 and time<21):
    print("Good Evening")
else:
    print("Good Night")