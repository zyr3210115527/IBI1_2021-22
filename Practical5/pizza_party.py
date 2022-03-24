n=1
while (n**2+n+2)/2<114514:
    if (n**2+n+2)/2>=64:
        message="We have "+str((n**2+n+2)/2)+" pizza now, it's enough for us."
        print(message)
        break
    else:
        n+=1
 
