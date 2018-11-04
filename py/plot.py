import matplotlib
import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from scipy import optimize

from matplotlib import rc
# rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
# rc('text', usetex=True)
plt.rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 20}

matplotlib.rc('font', **font)
plt.figure(figsize=(10,7)) 
plt.xlabel(r'{Температура,} $K^\circ$',labelpad=30)
plt.ylabel(r'{Мощность нелинейного отклика} $P_{3\omega}$, { a.u.}',labelpad=30)
# Make room for the ridiculously large title.
# plt.subplots_adjust(top=0.8)
plt.tight_layout()
# y,x = np.loadtxt('data/1r_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
# y,x = np.loadtxt('data/1c_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
# print(min(x))
# arr=np.vstack([x,y])
# np.savetxt('data/c.out', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays


x,y = np.loadtxt('data/cd.out', delimiter='\t', usecols=(0, 1), unpack=True)

R=np.array([0.85,1.08,1.55,2.15,2.88,3.87,4.97,6.25,7.67,9.32,11.14,13.12,15.08,17.22,19.32,21.44,23.57,25.7,27.83,29.95,32.06,34.15,36.25,38.34,40.42,42.49,44.56,46.63,48.69,50.75,52.8,54.84,56.88,58.92,60.96,62.98,65,67.01,69.02,71.03,73.03,75.02,77.01,79,80.98,82.97,84.94,86.93,88.9,90.89,92.86,94.83,96.8,98.76,100.72,102.67,104.62,106.56,108.51,110.45])
T=np.linspace(5,300,len(R))
# print(T)
# plt.plot(R,T,'*')


def u2r(u):
	return 1.3268*u+0.1163

def r2t(x):
	a = 22.04
	b = 2.452
	d = 11.11
	return b*(x+d)-a/x

x=r2t(u2r(x*1000))
# print(r2t(20.6))
# plt.plot(R,r2t(R))
# plt.show()

# print(u2r(24.8))

def remove(x):
	delete=[]
	for i in range(1,len(x)-1):
		if x[i+1]<=x[i]:
			for j in range(i+1,len(x)):
				if x[j]<=x[i]:
					delete.append(j)
				else:
					break
	delete.append(0)
	return delete

y=np.delete(y,remove(x))
x=np.delete(x,remove(x))

# for i in range(1,len(x)-1):
# 	if x[i+1]<=x[i]:
# 		print(x[i])

# arr=np.vstack([R,T])
# np.savetxt('data/RT.out', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays


i=np.where(x>92)
y=y-np.mean(y[i])
# plt.plot(x,y, 'ro', lw=0.8, markersize=0.5)
spl = UnivariateSpline(x, y)
xs = np.linspace(np.min(x), np.max(x), 10000)
spl.set_smoothing_factor(0.002)
plt.plot(xs, spl(xs), 'b', lw=2)
plt.xlim(min(x), 95)
plt.ylim(min(y), 1.2*max(y))
plt.show()
x2,y2 = np.loadtxt('data/c2.out', delimiter='\t', usecols=(0, 1), unpack=True)
x3,y3 = np.loadtxt('data/c3.out', delimiter='\t', usecols=(0, 1), unpack=True)





# plt.plot(x,y)
# x=x[0::40]
# y=y[0::40]
# plt.plot(x2,y2)
# plt.plot(x3,y3)
plt.show()