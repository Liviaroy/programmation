import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 500)
y = x ** 2

print(x)
print(y)

plt.plot(x,y)
plt.title("Fonction quadratique")
plt.show()


y = np.sin(x)

print(x)
print(y)

plt.plot(x,y)
plt.title("fonction sinusoidale")
plt.show()

y = 2 * x + 3


print(x)
print(y)

plt.plot(x,y)
plt.title("fonction linéaire")
plt.show()