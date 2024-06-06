def add(x,y):
    z=x+y;
    print("Summantion = ",z);


def subs(x,y):
    z=x-y;
    print("Subs = ",z);

def call_me(function_name,b,c):
    function_name(b,c)


 
call_me(add,5,6)
call_me(subs,5,6)