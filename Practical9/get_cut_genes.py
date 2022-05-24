import re

file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
a=file.read()
#open the file
b=re.compile(r'gene:(\S+).*?](.*?)>',re.S)
g=b.findall(a)
#Write DNA names and DNA sequences into a list

new_file=open('cut_genes.fa','w')
for i in range(len(g)):
    c=re.sub(r'\n','',g[i][1])
#Remove line breaks from the original file
    if "GAATTC" in c:
        new_file.write(">"+g[i][0]+"\n"+str(len(c))+"\n"+c+"\n")
        
        
        
        
        
