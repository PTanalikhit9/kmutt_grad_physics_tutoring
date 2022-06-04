import numpy as np
import matplotlib.pyplot as plt

xi = np.arange(0.01, 1, 0.01)

def G1(xi):
  K = 71.1 + 65.7*xi + 8.31*298*np.log((((1-xi)/(1+xi))**(1-xi))*(((2*xi)/(1+xi))**(2*xi)))
  return K

def G2(xi):
  P = 71.1 + 65.7*xi + 8.31*596*2.5*np.log(2)*(1+xi) + 8.31*596*np.log((((1-xi)/(1+xi))**(1-xi))*(((2*xi)/(1+xi))**(2*xi)))
  return P

plt.title('Gibbs free energy vs \u03BE')
plt.plot(xi, G1(xi), 'r', xi, G2(xi), 'b')
plt.legend(('T=298K, P=1atm, \u03BE','T=596K, P=1atm, \u03BE'))
plt.xlabel('\u03BE')
plt.ylabel('Gibbs free energy')
plt.show
