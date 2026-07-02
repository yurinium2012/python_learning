import numpy as np
import matplotlib.pyplot as plt


x= np.linspace(-10, 12, 100)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, color="g", label='Sine')
plt.plot(x, z, color="b", label='Cosine')
plt.plot(x, y + z, color="r", label='Sine + Cosine')
plt.xlabel("x")
plt.ylabel("trigonometric fn")
plt.grid("true")
plt.legend()
plt.show()