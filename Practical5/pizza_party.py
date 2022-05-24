n=1
#Set an initial value.
while (n**2+n+2)/2<114514: #Start the loop
    if (n**2+n+2)/2>=64:
        message_a="We've cut it "+str(n)+" times"+" and we have "+str((n**2+n+2)/2)+" pizza now, it's enough for us."
        print(message_a)#When the pizza quantity reaches the requirement, this result is output
        break
    elif n==1: #Solve the problem of singular and plural word "word"
        message_b="We've cut it "+str(n)+" time"+" and we have "+str((n**2+n+2)/2)+" pizza now, it isn't enough for us."
        print(message_b)
        n+=1 #The pizza quantity does not meet the requirements, the output results leave this cycle and enter the next cycle
    else:
        message_c="We've cut it "+str(n)+" times"+" and we have "+str((n**2+n+2)/2)+" pizza now, it isn't enough for us."
        print(message_c)
        n+=1 #The pizza quantity does not meet the requirements, the output results leave this cycle and enter the next cycle
 
