import numpy as np
import matplotlib.pyplot as plt

xi = np.arange(0.01, 1, 0.01)

def A1(xi):
  K = 65.7 + 8.31*298*np.log(((2*xi)**2)/((1-xi)/(1+xi)))
  return K

def A2(xi):
  P = 65.7 - 2.5*8.31*596*np.log(2) + 8.31*596*np.log(((2*xi)**2)/((1-xi)/(1+xi)))
  return P

plt.title('Affinity vs \u03BE')
plt.plot(xi, A1(xi), 'y', xi, A2(xi), 'p')
plt.legend(('T=298K, P=1atm, \u03BE','T=596K, P=1atm, \u03BE'))
plt.xlabel('\u03BE')
plt.ylabel('Affinity')
plt.show

xi = np.arange(0.01, 1, 0.01)
count = len(xi)
print('\u03BE        A(T1)    A(T2)')
for i in range(count):
    print("{:5.2f}".format(xi[i]),"{:10.2f}".format(A1(xi)[i]),"{:10.2f}".format(A2(xi)[i]))
