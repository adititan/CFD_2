import numpy as np
import matplotlib.pyplot as plt

def func_forward():
    x = np.float(np.pi/4.0)
    h = [0.0]
    result = []
    h[0] = np.float(np.pi/4.0)
    one = np.float(1.0)
    half = np.float(0.5)
    i = 0
    while(h[i] + one > one):
        result.append(np.float(abs(((np.sin(x+h[i]) - np.sin(x))/h[i])-np.cos(x))/np.cos(x)))
        h.append(h[i]*half)
        i +=1
    del h[-1]
    return h,result

def func_backward():
    x = np.float(np.pi/4.0)
    h = [0.0]
    result = []
    h[0] = np.float(np.pi/4.0)
    one = np.float(1.0)
    half = np.float(0.5)
    i = 0
    while(h[i] + one > one):
        result.append(np.float(abs(((np.sin(x) - np.sin(x-h[i]))/h[i])-np.cos(x))/np.cos(x)))
        h.append(h[i]*half)
        i +=1
    del h[-1]
    return h,result

def func_fourth_order():
    x = np.float(np.pi/4.0)
    h = [0.0]
    result = []
    h[0] = np.float(np.pi/4.0)
    one = np.float(1.0)
    half = np.float(0.5)
    eight = np.float(8.0)
    twelve = np.float(12.0)
    i = 0
    while(h[i] + one > one):
        t = (eight*np.sin(x+h[i]) - eight*np.sin(x-h[i]) - np.sin(x + np.float(2.0)*h[i]) + np.sin(x - np.float(2.0)*h[i]))/(h[i]*twelve)
        result.append(np.float(abs(t-np.cos(x))/np.cos(x)))
        h.append(h[i]*half)
        i +=1
    del h[-1]
    return h,result

def func_central():
    x = np.float(np.pi/4.0)
    h = [0.0]
    result = []
    h[0] = np.float(np.pi/4.0)
    one = np.float(1.0)
    half = np.float(0.5)
    i = 0
    while(h[i] + one > one):
        result.append(np.float(abs(((np.sin(x+h[i]) - np.sin(x-h[i]))/h[i]*half)-np.cos(x))/np.cos(x)))
        h.append(h[i]*half)
        i +=1
    del h[-1]
    return h,result

def plot():
    h1,result1 = func_forward()
    h2,result2 = func_backward()
    h3,result3 = func_central()
    h4,result4 = func_fourth_order()
    plt.figure()
    plt.loglog(h1,result1,label ='Forward')
    plt.loglog(h2,result2,label ='Backward')
    plt.loglog(h3,result3,label ='Central')
    plt.loglog(h4,result4,label ='Fourth_order')
    plt.legend()
    plt.title("Relative Error in calculation of derivatives with h(loglog)")
    plt.xlabel('log(h)')
    plt.ylabel('log(Relative Error)')
    plt.grid(True)
    #plt.show()
    plt.savefig('five.png')
    
plot()
