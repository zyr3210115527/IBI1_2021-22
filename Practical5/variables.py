a=19245301 #the cases in 2022
b=4218520 #the cases in 2021
c=271 #the cases in 2020
d=a-b
e=b-c
if d>e:
    print("d is greater")
if d<e:
    print("e is greater")
f=d/a
g=e/c
if g>f:
    print("the rate of new cases greater in 2020")
if f>g:
    print("the rate of new cases greater in 2021")

x=bool(input("x="))
y=bool(input("y="))
w=x and y
print (w)
