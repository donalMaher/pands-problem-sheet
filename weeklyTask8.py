import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,4,5)
fx = x**1
gx = x**2
hx = x**3
p=plt.plot(fx)
p=plt.plot(gx)
p=plt.plot(hx)
p=plt.legend(["fx","gx","hx"])
p=plt.title("Weekly Task 8")
plt.show(p)

