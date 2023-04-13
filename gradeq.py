import numpy as np
import sys
 
# function definition to compute magnitude of a vector
def magnitude(vector):
    return np.sqrt(sum(pow(element, 2) for element in vector))

# function to calculate the gradient of f
def grad(a, r):
    return 2*np.matmul(np.transpose(a), r)

# function to calculate the multiplicator gamma
def gamma(a, r):
    rtr = np.matmul(np.transpose(r),r)
    return -1/2.0*rtr/np.matmul(np.transpose(r),np.matmul(a, np.matmul(np.transpose(a),r)))

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

print(b)

print(a)

# initial guess
x = 1.0*np.array([0, 0, 0, 0, 0])

for i in range(50):
    r = np.matmul(a, x) - b
    
    gradienten = grad(a, r)
    gam = gamma(a, r)
    print(gam)
    g = gam*gradienten

    x += g

    print(x)
