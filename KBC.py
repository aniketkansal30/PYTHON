questions=[
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4],
    ["Which lang. was used to create FB?","Python","Java","C","C++","None",4]]
levels=[1000,2000,3000,5000,10000,20000,40000,60000,120000,240000,320000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"1. {question[1]}        2. {question[2]}")
    print(f"2. {question[3]}             4. {question[4]}")
    reply=int(input("Enter your answer(1-4) or 0  to quit: "))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"Correct answer, You have won Rs. {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong answer")
        break
print(f"Your take home money is {money}")        