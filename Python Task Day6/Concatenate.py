import numpy
P, N, M = map(int,input().split())
A = numpy.array([input().split() for i in range(P)],int)
B = numpy.array([input().split() for i in range(N)],int)
print(numpy.concatenate((A, B), axis = 0))