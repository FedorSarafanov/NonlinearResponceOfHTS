import matplotlib
import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp

from scipy.interpolate import UnivariateSpline

import matplotlib.pyplot as plt
from scipy import optimize

from matplotlib import rc
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 25}

matplotlib.rc('font', **font)

file='../data/RT.oo'

u,p = np.loadtxt(file, delimiter='\t', usecols=(0, 1), unpack=True)
# plt.plot(u,p)
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

# n=1200
# p=p[n:-1]
# u=u[n:-1]
# p=np.flip(p)
# u=np.flip(u)
#Удаление убывающих последовательностей
p=np.delete(p,remove(u))
u=np.delete(u,remove(u))

# #Удаление выбивающихся точек
# # i=np.where(abs(u)<abs(np.mean(u))/1.2)
# i=[]

# #Обрезка графика
# i=np.where((u<0.0163)|(u>0.0250))
# u=np.delete(u,i)
# p=np.delete(p,i)




# #Обрезка плато
# i=np.where(u>0.019)
# p=p-np.mean(p[i])

# i=np.where(p<0)
# # A=np.array(i)

# for j in np.nditer(i):
# 	p[j]=np.random.random_sample()/1000/2/2

# plt.plot(u,p)
# plt.show()

# arr=np.vstack([u,p])
# np.savetxt(file+'.clear', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays


x=u
y=p
spl = UnivariateSpline(x, y)
xs = np.linspace(np.min(x), np.max(x), 10000)
spl.set_smoothing_factor(1.8)
# plt.title('YBa$_2$Cu$_3$O$_7$')
# plt.xlabel('T',labelpad=15)
# plt.ylabel('R',labelpad=15)
plt.plot(spl(xs), xs*6.2, 'black', lw=2.7)
# plt.xlim(min(x), 95)
# plt.ylim(min(y), 1.2*max(y))
# plt.grid()
plt.xlim([50,150])
# plt.legend(TIT)
plt.tight_layout()
# top=0.955,
# bottom=0.104,
# left=0.084,
# right=0.955,
# hspace=0.2,
# wspace=0.2
plt.show()
# x2,y2 = np.loadtxt('data/c2.out', delimiter='\t', usecols=(0, 1), unpack=True)
# x3,y3 = np.loadtxt('data/c3.out', delimiter='\t', usecols=(0, 1), unpack=True)





# plt.plot(x,y)
# x=x[0::40]
# y=y[0::40]
# plt.plot(x2,y2)
# plt.plot(x3,y3)
# plt.show()