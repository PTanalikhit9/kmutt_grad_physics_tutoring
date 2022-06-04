import numpy as np
import matplotlib.pyplot as plt

xi = np.arange(0.01, 1, 0.01)

def G1(xi):
  K = 0.62 + 4.01*xi + 2476.38*(2*(1-xi)*np.log(1-xi) + 2*xi*np.log(0.5*xi))
  return K

def G2(xi):
  P = 0.62 + 4.01*xi + (1.72*10**4) + 4952.76*(2*(1-xi)*np.log(1-xi) + 2*xi*np.log(0.5*xi))
  return P

plt.title('Gibbs free energy vs xi')
plt.plot(xi, G1(xi), 'r', xi, G2(xi), 'b')
plt.legend(('T=298K, P=1atm','T=596K, P=1atm'))
plt.xlabel('xi')
plt.ylabel('Gibbs free energy')
plt.show
