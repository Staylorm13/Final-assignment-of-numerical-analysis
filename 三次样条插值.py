from matplotlib import pylab as plt
import numpy as np
from sympy import symbols, expand


def spline1(x0, y0, yx1, yxn, xk):
	# 根据式6-11，6-12，6-13
	# 求miu.lamda得A，求d后构造方程组，解方程得M=[M0,M1,M2,...]
	n = len(x0)
	miu = []
	lamda = []
	A = np.zeros((n, n), 'f')
	d = []
	h = [x0[1] - x0[0]]
	A[0, 0] = 2
	A[0, 1] = 1
	A[n - 1, n - 2] = 1
	A[n - 1, n - 1] = 2
	d.append(6 * ((y0[1] - y0[0]) / (x0[1] - x0[0]) - yx1) / (x0[1] - x0[0]))
	d.append(6 * (yxn - (y0[n - 1] - y0[n - 2]) / (x0[n - 1] - x0[n - 2])) / (x0[n - 1] - x0[n - 2]))
	for i in range(1, n - 1):
		h.append(x0[i + 1] - x0[i])
		miu.append(h[i - 1] / (h[i] + h[i - 1]))
		lamda.append(h[i] / (h[i - 1] + h[i]))
		A[i, i - 1] = miu[i - 1]
		A[i, i] = 2
		A[i, i + 1] = lamda[i - 1]
		d.insert(i, 6 * ((((y0[i + 1] - y0[i]) / h[i]) - ((y0[i] - y0[i - 1]) / h[i - 1])) / (h[i] + h[i - 1])))
	M = np.linalg.solve(A, d)
	
	# 代入6-8式得出三次样条表达式S
	x = symbols('x')
	S = []
	a1 = []
	a2 = []
	a3 = []
	a4 = []
	h = []
	for i in range(0, n - 1):
		h.append(x0[i + 1] - x0[i])
		a1.append(M[i] * (x0[i + 1] - x) ** 3 / (6 * h[i]))
		a2.append(M[i + 1] * (x - x0[i]) ** 3 / (6 * h[i]))
		a3.append((y0[i] - M[i] * h[i] ** 2 / 6) * (x0[i + 1] - x) / h[i])
		a4.append((y0[i + 1] - M[i + 1] * h[i] ** 2 / 6) * (x - x0[i]) / h[i])
	for i in range(0, n - 1):
		S.append(a1[i] + a2[i] + a3[i] + a4[i])
		Y = S[i]
		Y = expand(Y)
		print('第%d段三次样条插值函数：\n' % (i + 1), '当 x = (%8.5f, %8.5f) 时,\ny = ' % (x0[i], x0[i + 1]), Y, '\n')
	
	# 画图
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False
	plt.figure(figsize=(10, 8), dpi=100)
	plt.figure(1)
	# 画每段的三次样条插值函数
	for i in range(0, n - 1):
		plt.plot(x0[i], y0[i], 'bo', label='已知插值点')
		j = np.linspace(x0[i], x0[i + 1], 100)
		YY = []
		Y = S[i]
		for k in j:
			YY.append(Y.subs(x, k))
		plt.plot(j, YY, ':k')
	# 画待插值点
	for i in range(0, n - 1):
		if (x0[i] <= xk <= x0[i + 1]) or (x0[i] >= xk >= x0[i + 1]):
			Y = S[i]
			print('当待插值点x = %8.5f 时,代入插值函数得y(x) = %8.5f\n' % (xk, Y.subs(x, xk)))
			plt.plot(xk, Y.subs(x, xk), 'rp', label='待插值点')
			break
	
	plt.title('显示每个小段三次多项式的曲线')
	plt.legend(loc=1)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()


if __name__ == '__main__':
	x0 = np.array([27.7, 28, 29, 30])  # x0为已知节点
	y0 = np.array([4.1, 4.3, 4.1, 3])  # y0为已知函数值
	yx1 = 3  # yx1为函数在初始点的一阶导数值
	yxn = -4  # yxn为函数在末端点的一阶导数值
	xk = 28.5  # 待插值节点
	spline1(x0, y0, yx1, yxn, xk)
