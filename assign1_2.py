import numpy as np


def eps_float():
    eps = float(1.0)
    one = float(1.0)
    half = float(0.5)
    while( one +eps > one):
        eps = half*eps
#	print(eps)
    return eps

def eps_float_point():
    eps = float(1.0)
    one = float(1.0)
    point = float(0.1)
    while( one +eps > one):
        eps = point*eps
#	print(eps)
    return eps

def eps_float_ne():
    eps = float(1.0)
    one = float(1.0)
    half = float(0.5)
    while( one +eps != one):
        eps = half*eps
#	print(eps)
    return eps

def eps_float_sub():
    eps = float(1.0)
    one = float(1.0)
    half = float(0.5)
    while( one -eps < one):
        eps = half*eps
#	print(eps)
    return eps

def eps_float_ten():
    eps = float(1.0)
    ten = float(10.0)
    half = float(0.5)
    while( ten +eps > ten):
        eps = half*eps
#	print(eps)
    return eps

def eps_float128():
    eps = np.float128(1.0)
    one = np.float128(1.0)
    half = np.float128(0.5)
    while(one-eps < one):
        eps = half*eps
    return eps


print("Machine epsilon for float data type in python: ",eps_float())
print("Machine epsilon for float data type in python: ",eps_float_point())
print("Machine epsilon for float data type in python: ",eps_float_ne())
print("Machine epsilon for float data type in python: ",eps_float_sub())
print("Machine epsilon for float data type in python: ",eps_float_ten())

#print("Machine epsilon for numpy.float128 data type in python: ",eps_float128())
