import numpy as nn
import matplotlib.pyplot as mpl

x = nn.linspace(0,2*nn.pi,100)
y = nn.sin(x)
z = nn.cos(y)

mpl.plot(x,y, marker="x", color="black", label='sin(x)')
mpl.plot(x,y, color="orange", label='cos(x)')


mpl.title("evenly spaced numbers")
mpl.xlabel("xxxx")
mpl.ylabel("yyyy")
mpl.grid("true")
mpl.legend()
mpl.show()