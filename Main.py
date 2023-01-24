#Code to find which number is smaller by conditional statement (if-elif-else) by only 3 attempts

num1=int(input("enter the 1st num"))
num2=int(input("enter the 2nd num"))
num3=int(input("enter the 3rd num"))

if ("num1>num2")and ("num1>num3")and("num1!num2")and("num1!num3"):
    print(f"in this progarm",{num1},"is smaller than",{num2},{num3})


elif ("num2>num1")and ("num2>num3")and("num2!num1")and("num2!num3"):
    print(f"in this Set of Numbers",{num2},"is smaller than",{num1},{num3})


elif ("num3>num2")and ("num3>num1")and ("num3!num2")and("num3!num1"):
    print(f"in this set of Numbers",{num3},"is smaller than",{num1},{num2})


else:
    print("all number are eqaul")