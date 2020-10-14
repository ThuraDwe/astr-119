import numpy as np #import numpy library

#intgers
i = 10  #integer
print(type(i)) #print out the type of i

a_i = np.zeros(i,dtype=int) #an array of ints
print(type (a_i)) #print out the type
print(type (a_i[0])) #print out the type


#floats
x = 119.0 #floating point number
print(type(x)) #print out the type

y = 1.19e2 #sci not float
print (type(y)) #print out the type

z = np.zeros(i,dtype=float) #declare an array of floats
print(type(z)) #will return nd array
print(type(z[0])) #will return float64

