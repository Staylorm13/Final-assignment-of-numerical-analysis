import numpy as np
from matplotlib import pylab as plt
from sympy import *


class bijin(object):
	def __init__(self, f, a, b, n):
		self.f = f     # 逼近函数
		self.a = a     # 区间左端点
		self.b = b     # 区间右端点
		self.n = n     # 多项式次数
	
	def fun1(self):
		f = self.f
		a = self.a
		b = self.b
		n = self.n
		G = np.zeros([n + 1, n + 1], 'f')
		x = symbols('x')
		f = sympify(f)
		
		# 求希尔伯特矩阵
		for i in range(n + 1):
			for j in range(n + 1):
				G[i][j] = integrate(x ** (i + j), (x, a, b))
				
		# 求d（右端列向量）
		d = np.zeros([n + 1, 1], 'f')
		for i in range(n + 1):
			d[i] = integrate(f*(x**i), (x, a, b))
			
		# 解线性方程组，得系数A=[a0,a1,a2...]
		A = np.linalg.solve(G, d)
		result = 0.0
		for i in range(n + 1):
			result = result + A[i] * (x ** i)
		result = result[0]
		
		# 输出
		print('G:\n', G)
		print('d：\n', d)
		print('多项式系数为:\n', A)
		print('最佳平方逼近多项式为：\n', result)
		# 画图
		plt.rcParams['font.sans-serif'] = ['SimHei']
		plt.rcParams['axes.unicode_minus'] = False
		plt.figure(figsize=(10, 8), dpi=100)
		plt.figure(1)
		# 画原函数点
		xx = np.linspace(1, 2, 10)
		yy = []
		for i in xx:
			yy.append(f.subs(x, i))
		plt.plot(xx, yy, 'k*', label='插值点')
		# 画逼近多项式
		xx = np.linspace(1, 2, 1000)
		yy = []
		for i in xx:
			yy.append(result.subs(x, i))
		plt.plot(xx, yy, 'b--', label='最佳平方逼近多项式')
		
		plt.title('最佳平方逼近法')
		plt.xlabel('x')
		plt.ylabel('y')
		plt.legend(loc=1)
		plt.show()


if __name__ == '__main__':
	x = symbols('x')
	f = sqrt(1+x**2)
	f = sympify(f)
	a = 0
	b = 1
	n = 3
	bj = bijin(f, a, b, n)
	bj.fun1()
