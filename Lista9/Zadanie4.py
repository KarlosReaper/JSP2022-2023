import math
import numpy
import matplotlib.pyplot as plt

#
# Zadanie 4
#
print('Zadanie 4')

pop = [16.66, 16.56, 11.94, 11.82, 4.92, 3.94, 3.19, 2.22, 1.87, 1.62]
naz = ['Python', 'C', 'C++', 'Java', 'C#', 'Visual Basic', 'JavaScript', 'SQL', 'Assembly language', 'PHP']
y_pos = numpy.arange(len(pop))
plt.bar(y_pos, pop)
plt.xticks(y_pos, naz)
plt.xlabel('Jezyk programowania')
plt.ylabel('Popularnosc [%]')
plt.title('10 najpopularniejszych jezykow programowania')
plt.show()