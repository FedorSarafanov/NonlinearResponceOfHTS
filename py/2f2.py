import matplotlib
import numpy as np
from numpy import pi,cos,sin,abs,sqrt,exp
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from scipy import optimize

files=['data/1a_p3w',
	'data/1b_p3w',
	'data/1b_p3w2',
	'data/1c_p3w',
	'data/1l_p3w',
	'data/1r_p3w']
for file in files:
	pass
	p,u = np.loadtxt(file, delimiter='\t', usecols=(1, 3), unpack=True)
	# y,x = np.loadtxt('data/1c_p3w', delimiter='\t', usecols=(1, 3), unpack=True)
	# print(min(x))
	arr=np.vstack([u,p])
	np.savetxt(file+'.tsv', arr.T,delimiter='\t', fmt='%f')   # x,y,z equal sized 1D arrays