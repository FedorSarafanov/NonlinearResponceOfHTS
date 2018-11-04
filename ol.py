import matplotlib
import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from scipy import optimize

from matplotlib import rc

# fig = matplotlib.pyplot.gcf()
# fig.set_size_inches(6, 5)

# for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
# rc('text', usetex=True)
# plt.rc('text', usetex=True)
# rc('text.latex',unicode=True)
# rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
# rc('text.latex',preamble=r'\usepackage[russian]{babel}')
# rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans']})

# font = {'family' : 'serif',
#         'weight' : 'bold',
#         'size'   : 23}

# matplotlib.rc('font', **font)
# plt.figure(figsize=(10,7)) 
# plt.xlabel(r'{Температура,} $K**\circ$',labelpad=10)
# plt.ylabel(r'{Мощность нелинейного отклика} $P_{3\omega}$, { a.u.}',labelpad=30)
# # Make room for the ridiculously large title.
# # plt.subplots_adjust(top=0.8)
# plt.tight_layout()
# y,x = np.loadtxt('data/1r_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
# y,x = np.loadtxt('data/1c_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
# print(min(x))
# arr=np.vstack([x,y])
# np.savetxt('data/c.out', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays

def f(x):
	a1 =      0.1929
	b1 =       0.514
	c1 =     0.05736
	a2 =      0.2376
	b2 =       0.427
	c2 =      0.1809
	a3 =      0.4866
	b3 =      0.5678
	c3 =      0.1187
	return a1*exp(-((x-b1)/c1)**2) + a2*exp(-((x-b2)/c2)**2) + a3*exp(-((x-b3)/c3)**2)

def r(x):
	b=-0.9
	a=23
	return 1/(1+exp(-2*a*(x+b)))

def i(T):
	a =    -0.00142
	b =       3.982
	c =      0.8263
	d =      -4.253
	# return a*exp(b*x) + c*exp(d*x)
	H0=0.4
	Tc=0.8
	return H0*(1-(T/Tc)**2) 

x=np.linspace(0,0.8,1000)
x2=np.linspace(0.8,1,1000)
# f=np.exp(-0.5*(x-4)**2)+0.5*np.exp(-0.1*(x-6)**2)

fi=f(x)
fa=i(x)+0.01
fi=fi/np.max(fi)
fa=fa#/np.max(fa)
rr=r(x2)
rr=rr/np.max(rr)
arr=np.vstack([x,fi,fa])
np.savetxt('data/12.out', arr.T,delimiter='\t', fmt='%f',header='x	y	z',comments='')   # x,y,z equal sized 1D arrays
arr=np.vstack([x2,rr])
np.savetxt('data/3.out', arr.T,delimiter='\t', fmt='%f',header='x	y',comments='')   # x,y,z equal sized 1D arrays
plt.plot(x,fi)
plt.plot(x,fa)
plt.plot(x2,rr)
plt.show()