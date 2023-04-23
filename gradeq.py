import numpy as np
import sys
 
# function definition to compute magnitude of a vector
def magnitude(vector):
    return np.sqrt(sum(pow(element, 2) for element in vector))

# function to calculate the gradient of f
def grad(a, r):
    return 2*np.matmul(np.transpose(a), r)

# function to calculate the multiplicator gamma
def gamma(m, r):
    rtr = np.matmul(np.transpose(r),r)
    return -1/2.0*rtr/np.matmul(np.transpose(r),np.matmul(m,r))

# Read the vector, b and matrix, a from file. 
# Elements seperated by space. 
# Filename given as argument
with open(sys.argv[1], 'r') as f:
    b_string = f.readline().split(' ')
    n = int(len(b_string))
    b = np.zeros(n)
    a = np.zeros([n, n])
    for i in range(n):
        b[i] = int(b_string[i])

    for i in range(n):
        a_string = f.readline().split(' ')
        for j in range(n):
            a[i, j] = int(a_string[j])

x_string = input("Ge " + str(n) + " startvärden för x separerade med mellanslag :  ").split(' ')
x = [0.0]*n

for i in range(n):
    x[i] = float(x_string[i])
    
print(b)

print(a)

m = np.matmul(a, np.transpose(a))

r = np.matmul(a, x) - b

i = 0
while i < 1000 and magnitude(r) > 0.01:
    
    gradienten = grad(a, r)
    gam = gamma(m, r)
    print(gam)
    g = gam*gradienten

    x += g

    r = np.matmul(a, x) - b
    print("r = ",magnitude(r))
    print("x = ", x)

    i += 1
print("Klart efter ", i , " iterationer")