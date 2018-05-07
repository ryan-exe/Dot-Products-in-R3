import sys
V = sys.argv[1:4] # Assigning the vector v with the first set of numbers
U = sys.argv[4:7] # Assigning the vector u with the second set of numbers
dot_product = int(V[0])*int(U[0]) + int(V[1])*int(U[1]) + int(V[2])*int(U[2]) # Multiples each number of the same index together then adds the results
print("V = {{ {}, {}, {} }}".format(V[0],V[1],V[2])) # Prints vector V
print("U = {{ {}, {}, {} }}".format(U[0],U[1],U[2])) # Prints vector U
print("V . U = " + str(dot_product)) # Prints the result of the dot product