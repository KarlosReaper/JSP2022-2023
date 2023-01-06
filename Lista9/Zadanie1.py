import math
import numpy

#
# Zadanie 1
#
print('Zadanie 1')

# Deklaruje tablice ze wspolczynnikami
A = numpy.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
B = numpy.array([6,2,-5,17,12]).T

solution = numpy.linalg.solve(A,B)
print('Rozwiazanie ukladu to: ', end='\n')
print('x = ',solution[0], end='\n')
print('y = ',solution[1], end='\n')
print('z = ',solution[2], end='\n')
print('t = ',solution[3], end='\n')
print('u = ',solution[4], end='\n')