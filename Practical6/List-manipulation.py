import matplotlib.pyplot as plt
import numpy as np
print("Rob's marks in this course is:")
marks=[45,36,86,57,53,92,65,45]
a=sorted(marks)
print(a)#print a list of sorted value for marks.
plt.style.use('_mpl-gallery')#change the style of the boxplot.
plt.boxplot(marks)
plt.show()#Show the boxplot.
averange=np.mean(marks)
message="Rob's averange marks is "+str(averange)+"."
print(message)
if averange<60:
    print("He cannot pass the course.")
else:
    print("He can pass the course.")#Judge whether rob can pass the course.

