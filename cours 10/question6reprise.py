import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10)
y = x ** 2
plt.plot(x, y)
plt.show()

x = np.linspace(-10, 10)
y = np.sin(x)
plt.plot(x,y)
plt.show()

x = np.linspace(-10, 10)
y = 2 *x + 3
plt.plot(x,y)
plt.show()
