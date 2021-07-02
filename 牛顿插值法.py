import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sympy import symbols, sympify


def get_diff_table(x0, y0):
	"""
	得到插商表
	"""
	Y = np.zeros([len(x0), len(x0)])
	for i in range(0, len(x0)):
		Y[i][0] = y0[i]
	
	for j in range(1, len(x0)):
		for i in range(j, len(x0)):
			Y[i][j] = (Y[i][j - 1] - Y[i - 1][j - 1]) / (x0[i] - x0[i - j])
	return Y


def newton_interpolation(x0, y0, x):
	"""
	计算x点的插值
	"""
	Y = get_diff_table(x0, y0)
	y = Y[0, 0]
	k = 1
	for i in range(1, len(x0)):
		k = k * (x - x0[i - 1])
		y += Y[i, i] * k  # 得出结果
	return y


def loss(x0, y0, x1, y1):
	# w = eval(Wn(x0, len(x0)))  # 误差分析部分，求截断误差
	k = 1
	for i in range(1, len(x0)):
		k = k * (x - x0[i - 1])
	w = sympify(k)
	x0.append(x1)
	y0.append(y1)
	Y = get_diff_table(x0, y0)
	Loss = abs(w.subs(x, x1) * Y[len(x0) - 1, len(x0) - 1])
	return Loss


if __name__ == '__main__':
	
	# 初始值
	a = np.linspace(1, 11, 11)
	b = [16.08, 17.08, 21.42, 30.67, 27.67, 32.08, 34.5, 34.92, 36.25, 36.25, 37]
	x0 = ([2, 6, 9])
	y0 = ([17.08, 32.08, 36.25])
	
	# 输出差商表
	Y = get_diff_table(x0, y0)
	df = pd.DataFrame(Y)
	print('插值表：\n', df)
	
	# 输出牛顿基本插值多项式
	x = symbols('x')
	y = newton_interpolation(x0, y0, x)
	print('所得牛顿基本插值多项式为：\n', 'y=', y)
	
	# 输出预测值
	x1 = 8
	G = sympify(y)
	y1 = G.subs(x, x1)
	print('预测值:\n', '当x = %.4f时，y(x) = %.7f' % (x1, y1))
	
	# 输出截断误差
	Loss = loss(x0, y0, x1, y1)
	print('截断误差为：\n', Loss)
	
	xs = np.linspace(np.min(x0), np.max(x0), 1000, endpoint=True)
	ys = []
	for x in xs:
		ys.append(newton_interpolation(x0, y0, x))
	
	# 画图
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False
	plt.figure(figsize=(10, 8), dpi=100)
	plt.figure(1)
	plt.plot(a, b, '*k')
	plt.plot(x0, y0, 'bp', label="插值点")  # 蓝点表示原来的值
	plt.plot(xs, ys, 'r--', label='牛顿基本插值多项式')  # 插值曲线
	plt.plot(x1, y1, 'ro', label='预测点')  # 预测点
	plt.title("牛顿插值法")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend(loc=4)  # 指定legend的位置右下角
	plt.show()

# 已写好，勿改