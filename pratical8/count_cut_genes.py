import re

a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
b=a.read()
#open the file
e=re.compile(r'gene:(\S+).*?](.*?)>',re.S)
c=e.findall(b)
#Write the DNA name and DNA sequence into a list.
word=input('The filename is: ')
new_file=open(word,'w')

for i in range(len(c)):
    d=re.sub(r'\n','',c[i][1])
#Remove line breaks from the original file
    f=re.findall('GAATTC',d)
    if 'GAATTC' in d:
        new_file.write('>'+c[i][0]+" "+str(len(f)+1)+'\n'+d+'\n')

