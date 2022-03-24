n=1
while (n**2+n+2)/2<114514:
    if (n**2+n+2)/2>=64:
        message_a="We've cut it "+str(n)+" times"+" and we have "+str((n**2+n+2)/2)+" pizza now, it's enough for us."
        print(message_a)
        break
    elif n==1: #Solve the problem of singular and plural word "word"
        message_b="We've cut it "+str(n)+" time"+" and we have "+str((n**2+n+2)/2)+" pizza now, it isn't enough for us."
        print(message_b)
        n+=1
    else:
        message_c="We've cut it "+str(n)+" times"+" and we have "+str((n**2+n+2)/2)+" pizza now, it isn't enough for us."
        print(message_c)
        n+=1
 
