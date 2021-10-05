# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import copy as cp 
import numpy as np
import matplotlib.pyplot as plt

my_file=open("/amuhome/m18024598/CMB/TP2/input","r")
data = my_file.read()
my_file.close ()
data_splitted = data.split("\n")
#print(data)


n=len(data_splitted[:][1])
m=len(data_splitted[0])
array = [[int(data_splitted[line][column]) for  column  in  range(m)] for  line in  range(n)]


def count_neighbours(i,j,array) :
    sum_nbours = (
        array[i-1][j-1] + array[i-1][j] + array[i-1][j+1] 
        + array[i][j-1] + array[i][j+1] 
        + array[i+1][j-1] + array[i+1][j] + array[i+1][j+1]
        )
    return sum_nbours


for i in range(1,n-1):
    for j in range(1,m-1):
        sum_nbours = count_neighbours(i, j, array)
    
        
def cell_next_state(state,sum_nbours) :
    if state == 0:
        if sum_nbours == 3: 
            return 1
        return 0
    if state == 1:
        if 2 > sum_nbours or 3 < sum_nbours:
            return 0
        return 1


def next_state(array):
    array2 = cp.deepcopy(array)
    for i in range(1,n-1):
        for j in range(1,m-1):
            array2[i][j]= cell_next_state(array[i][j], count_neighbours(i, j, array))
    return array2

def repetition(array,k):
    for t in range(k):
        array = next_state(array)
    return array

#print(repetition(array, 2))

output = repetition(array, 100)
plt.imshow(output)
plt.show()
    
output_file = open("output.txt","w+")
for i in range(1,n):
    for j in range(1,m):
        output_file.write(str(output[i][j]))
    output_file.write("\n")

    



        


        


