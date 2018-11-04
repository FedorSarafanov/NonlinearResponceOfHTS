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
# plt.rc('text', usetex=True)
# rc('text.latex',unicode=True)
# rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
# rc('text.latex',preamble=r'\usepackage[russian]{babel}')

# font = {'family' : 'serif',
#         'weight' : 'bold',
#         'size'   : 20}

# matplotlib.rc('font', **font)
# plt.figure(figsize=(10,7)) 
# plt.xlabel(r'{Температура,} $K^\circ$',labelpad=30)
# plt.ylabel(r'{Мощность нелинейного отклика} $P_{3\omega}$, { a.u.}',labelpad=30)
# # Make room for the ridiculously large title.
# # plt.subplots_adjust(top=0.8)
# plt.tight_layout()
# y,x = np.loadtxt('data/1r_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
# y,x = np.loadtxt('data/1c_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
# print(min(x))
# arr=np.vstack([x,y])
# np.savetxt('data/c.out', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays


file='data/1c_p3w.tsv'

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

n=7300
p=p[n:-1]
u=u[n:-1]
p=np.flip(p)
u=np.flip(u)
#Удаление убывающих последовательностей
p=np.delete(p,remove(u))
u=np.delete(u,remove(u))

#Удаление выбивающихся точек
# i=np.where(abs(u)<abs(np.mean(u))/1.2)
i=[]

#Обрезка графика
i=np.where((u<0.0163)|(u>0.0250))
u=np.delete(u,i)
p=np.delete(p,i)




#Обрезка плато
# i=np.where(u>0.019)
# p=p-np.mean(p[i])

# i=np.where(p<0)
# A=np.array(i)

# for j in np.nditer(i):
	# p[j]=np.random.random_sample()/1000/2/2

plt.plot(u,p)
plt.show()

# arr=np.vstack([u,p])
# np.savetxt(file+'.clear', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays


# print(u2r(24.8))

# def remove(x):
# 	delete=[]
# 	for i in range(1,len(x)-1):
# 		if x[i+1]<=x[i]:
# 			for j in range(i+1,len(x)):
# 				if x[j]<=x[i]:
# 					delete.append(j)
# 				else:
# 					break
# 	delete.append(0)
# 	return delete

# y=np.delete(y,remove(x))
# x=np.delete(x,remove(x))

# for i in range(1,len(x)-1):
# 	if x[i+1]<=x[i]:
# 		print(x[i])

# arr=np.vstack([R,T])
# np.savetxt('data/RT.out', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays


# i=np.where(x>92)
# y=y-np.mean(y[i])
# # plt.plot(x,y, 'ro', lw=0.8, markersize=0.5)
# spl = UnivariateSpline(x, y)
# xs = np.linspace(np.min(x), np.max(x), 10000)
# spl.set_smoothing_factor(0.002)
# plt.plot(xs, spl(xs), 'b', lw=2)
# plt.xlim(min(x), 95)
# plt.ylim(min(y), 1.2*max(y))
# plt.show()
# x2,y2 = np.loadtxt('data/c2.out', delimiter='\t', usecols=(0, 1), unpack=True)
# x3,y3 = np.loadtxt('data/c3.out', delimiter='\t', usecols=(0, 1), unpack=True)





# plt.plot(x,y)
# x=x[0::40]
# y=y[0::40]
# plt.plot(x2,y2)
# plt.plot(x3,y3)
# plt.show()