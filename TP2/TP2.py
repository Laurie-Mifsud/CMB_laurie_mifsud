# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import copy as cp 

my_file=open("/amuhome/m18024598/CMB/TP2/input","r")
data = my_file.read()
my_file.close ()

data_splitted = data.split("\n")
#print(data_splitted)
#print(data)


N0=len(data_splitted)
N1=len(data_splitted[0])

#array = [[int(data_splitted[i][j]) for j in  range(N1)] for i in  range(N0-1)]
#print("array=",array)


array2 = [[int(data_splitted[line][column]) for  column  in  range(N1)] for  line in  range(N0-1)]
#print(array2)

def count_neighbours(i,j,matrice) :
    sum_nbours = sum(matrice[i-1][j-1:j+2])
    sum_nbours = sum_nbours + sum(matrice[i][j-1:j+2]) - matrice[i][j]
    sum_nbours = sum_nbours + sum(matrice[i+1][j-1:j+2])
    return sum_nbours


n=len(array2)
m=len(array2[0])

for i in range(1,n-1):
    for j in range(1,m-1):
        sum_nbours = count_neighbours(i, j, array2)
        
def cell_next_state(state,sum_nbours) :
    if state == 0:
        if sum_nbours == 3: 
            return 1
        return 0
    if state == 1:
        if 2 > sum_nbours or 3 < sum_nbours:
            return 0
        return 1

def next_state(matrice):
    array3 = [] 
    for i in range(1,n-1):
        line = []
        for j in range(1,m-1):
            next = cell_next_state(matrice[i][j], count_neighbours(i, j, array2))
            line.append(next)
        array3.append(line)
    return array3

print(next_state(array2))

def repetition(matrice,k):
    matrice2 = matrice.copy()
    for n in range(k):
        matrice2 = next_state(matrice2)
    return matrice2

print(repetition(array2, 49))


    

    



        


        


