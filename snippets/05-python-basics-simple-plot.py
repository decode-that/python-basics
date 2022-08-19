# Simple Plot Example
# Using Matplotlib Library
import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(0,2*np.pi,50)
y_vals = np.sin(x_vals)
y_vals2 = np.cos(x_vals)

plt.plot(x_vals,y_vals,label='sine')
plt.plot(x_vals,y_vals2,label='cosine')
plt.legend()