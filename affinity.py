import numpy as np
import matplotlib.pyplot as plt

xi = np.arange(0.01, 1, 0.01)

def A1(xi):
  K = 4.01 + 2476.38 * (2*np.log(xi) - np.log(4*(1-xi)**2))
  return K

def A2(xi):
  P = 4.01 + 4952.76 * (2*np.log(xi) - np.log(4*(1-xi)**2))
  return P

plt.title('Affinity vs xi')
plt.plot(xi, A1(xi), 'y', xi, A2(xi), 'p')
plt.legend(('T=298K, P=1atm','T=596K, P=1atm'))
plt.xlabel('xi')
plt.ylabel('Affinity')
plt.show
