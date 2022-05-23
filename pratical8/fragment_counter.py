import re

gene='ATGCAATCGACTACGATCAATCGAGGGCC'
a = re.findall('GAATTC',gene)
#Find qualified sequences
print("The number of the fragment(s) is "+str(len(a)+1))
#Output the number of the fragment(s).
