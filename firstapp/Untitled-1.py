from random import *
matrix=[]
summ=0
for i in range(5):
    line=[]
    for d in range(5):
        element=randint(0,100)
        line.append(element)
    matrix.append(line)
for t in range(len(matrix)):
    summ+=matrix[t][0]
print(summ)
for k in range(len(matrix)):
    for u in range(len(matrix[k])):
        print(matrix[k][u] , end=" ")
    print()
