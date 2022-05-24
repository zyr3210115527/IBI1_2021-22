def base_ratio(sequence):
    n=0
    a=0
    t=0
    c=0
    g=0
    b=sequence.upper()
#Convert letters to uppercase
    d=list(b)
    for i in range(len(sequence)):
         if d[i]=='A':
            a+=1
            n+=1
         elif d[i]=='T':
            t+=1
            n+=1
         elif d[i]=='C':
            c+=1
            n+=1
         elif d[i]=='G':
            g+=1
            n+=1
    aa=a/n
    tt=t/n
    cc=c/n
    gg=g/n
    message_a=("The rate of the A is "+str(aa))
    message_t=("The rate of the T is "+str(tt))
    message_c=("The rate of the C is "+str(cc))
    message_g=("The rate of the A is "+str(gg))
    print(message_a+"\n"+message_t+'\n'+message_c+'\n'+message_g)
#Define a function
a="atgcatcgaTgctacgatgctaGcatgcataAttcg"
base_ratio(a)
#Take an example
print("The sequence is ")
sequence=input()
base_ratio(sequence)
    
    


