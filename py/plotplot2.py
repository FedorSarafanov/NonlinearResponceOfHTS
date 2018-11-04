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

font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 23}

matplotlib.rc('font', **font)
plt.figure(figsize=(10,7)) 
plt.xlabel(r'Температура, K',labelpad=15)
plt.ylabel(r'Мощность отклика $P_{3\omega}$, a.u.',labelpad=30)
# # Make room for the ridiculously large title.
# # plt.subplots_adjust(top=0.8)
# plt.tight_layout()
# y,x = np.loadtxt('data/1r_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
# y,x = np.loadtxt('data/1c_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
# print(min(x))
# arr=np.vstack([x,y])
# np.savetxt('data/c.out', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays

files=['data/1a_p3w',
	# 'data/1b_p3w',
	'data/1b_p3w2',
	# 'data/1c_p3w',
	'data/1l_p3w',
	'data/1r_p3w'
	]

def u2r(u):
	return 1.3268*u+0.1163

def r2t(x):
	a = 22.04
	b = 2.452
	d = 11.11
	return b*(x+d)-a/x

from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('multipage.pdf')
SMF=[0.002,0.002,0.002,0.002,0.002,]
# TIT=['Верхняя точка','Нижняя точка', 'Центральная точка','Левая точка','Правая точка']
TIT=['Верхняя точка','Нижняя точка', 'Правая точка','Левая точка','Правая точка']
i=0
for file in files:
	smf=SMF[i]
	u,p = np.loadtxt(file+'.tsv.clear', delimiter='\t', usecols=(0, 1), unpack=True)
	p=p/np.max(p)
	u=r2t(u2r(u*1000))

	x=u
	y=p

	spl = UnivariateSpline(x, y)
	xs = np.linspace(np.min(x), np.max(x), 10000)
	spl.set_smoothing_factor(0.005)
	plt.grid()
	# plt.xlabel('Температура, К')
	# plt.ylabel('Мощность третей гармоники, условных единиц')
	# plt.title(TIT[i])
	i+=1
	plt.plot(xs, spl(xs),  lw=2)
	plt.xlim(min(x), 92)
	# plt.show()

	# plt.savefig(pp, format='pdf')
	# plt.close()

	# pp.savefig()
	# plt.ylim(min(y), 85)

	# plt.plot(u,p)
plt.grid()
# plt.legend(TIT)
plt.tight_layout()
plt.show()

# .pp.close()

