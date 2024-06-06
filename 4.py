def add(x,y):
    z=x+y;
    print("Summantion = ",z);


def subs(x,y):
    z=x-y;
    print("Subs = ",z);



a=int(input("Enter Num1"))
b=int(input("Enter Num2"))
c=input("Enter Operator")


if(c=="+"):
    add(a,b)
elif(c=="-"):
    subs(a,b)
else:
    print("Invalid Operator")
