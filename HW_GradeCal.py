score = float(input("Enter your score : "))
grade = ["A","B","C","D","F"]
if score>=80 and score <=100:
    print(f"Grade : {grade[0]}")
elif score<80 and score>=70 :
    print(f"Grade : {grade[1]}")
elif score<70 and score>=60 :
    print(f"Grade : {grade[2]}")
elif score<60 and score>=50 :
    print(f"Grade : {grade[3]}")
elif score<50 and score>=0 :
    print(f"Grade : {grade[4]}")
else :
    print("your score was wrong type again")