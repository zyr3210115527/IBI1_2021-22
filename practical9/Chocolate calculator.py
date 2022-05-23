def f(x,y):
    a=int(x)//int(y)
    b=int(x)-a*int(y)
    print("You can buy "+str(a)+" chocolete(s) and there are "+str(b)+" yuan left.")
    return a
    return b
x=30
y=4
f(x,y)
#Take an example
print("How much money do you have")
m=input()
print("How much for one chocolete")
n=input()
f(m,n)
