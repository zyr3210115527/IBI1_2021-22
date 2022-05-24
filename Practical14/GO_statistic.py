import matplotlib.pyplot as plt
from xml.dom.minidom import parse 
import xml.dom.minidom
import numpy as np
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
term_list=collection.getElementsByTagName("term")
print("The number of the terms is: ")
print(len(term_list))
#Output the number of the terms.

data={}
childnode={}
translation=[]

for term in term_list:
    id=term.getElementsByTagName('id')[0].childNodes[0].data
    data[id]=[]
    childnode[id]={id:0}
for term in term_list:
    name=term.getElementsByTagName('id')[0].childNodes[0].data
    is_a=term.getElementsByTagName('is_a')
    for x in is_a:
        data[x.childNodes[0].data].append(name)
    if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data.lower():
        translation.append(name)
def recursion(term,e):
    child_list=data[term]
    for child in child_list:
        if childnode[child]=={child:0}:
            e.append(child)
            for i in e:
                childnode[i][child] = 0
            recursion(child,e)
            del e[-1]
        else:
            for i in e:
                childnode[i].update(childnode[child])
all_term_childnode=[]
#The list of all total childnodes
translation_list=[]
#The list of translation
for a in data.keys():
    b=[a]
    recursion(a,b)
    all_term_childnode.append(len(childnode[a].keys())-1)
    if a in translation:
        translation_list.append(len(childnode[a].keys())-1)    
# draw the boxplot
plt.subplot(2,2,1)
plt.boxplot(all_term_childnode)
plt.title('all GO terms')
plt.xlabel("all GO terms")
plt.ylabel("Number")
plt.subplot(2,2,2)
plt.boxplot(translation_list)
plt.title('terms associated with translation')
plt.xlabel("associated with translation")
plt.ylabel("Number")
plt.show()
print("The average of childnodes of all terms is: ",np.average(all_term_childnode))
print("The average of childnodes of terms associated with translation is: ",np.average(translation_list))

#Translation terms contain smaller number of child nodes than the overall GO.

