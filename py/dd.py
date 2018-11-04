import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms=5)
# Use the default value for the smoothing parameter:

def remove(x):
	delete=[]
	for i in range(1,len(x)-1):
		if x[i+1]<=x[i]:
			for j in range(i+1,len(x)):
				if x[j]<=x[i]:
					delete.append(j)
				else:
					break
	return delete
# print(delete)

print(x)
# spl = UnivariateSpline(x, y)
# xs = np.linspace(-3, 3, 1000)
# # plt.plot(xs, spl(xs), 'g', lw=3)
# # Manually change the amount of smoothing:


# spl.set_smoothing_factor(0.01)
# plt.plot(xs, spl(xs), 'b', lw=3)
# plt.show()