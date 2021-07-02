from matplotlib.pyplot import gca
from sympy import symbols
from sympy.abc import x
from matplotlib import pyplot as plt
import numpy as np


def qiu_gen(f, x1, xn, err):
	n = 1
	er = 1
	x=symbols('x')
	y1 = f.subs(x, x1)
	x2 = (x1 + xn) / 2
	y2 = f.subs(x, x2)
	while er > err:
		n += 1
		er = abs(x1 - xn)
		if y1 * y2 > 0:
			x1 = x2
			x2 = (x2 + xn) / 2
			y1 = f.subs(x, x1)
			y2 = f.subs(x, x2)
			continue
		elif y1 * y2 < 0:
			x2 = (x1 + x2) / 2
			y2 = f.subs(x, x2)
			continue
		else:
			break
			
	# 输出
	print('经过%d次二分后，方程的根为：\n' % n, x2)
	# 画图
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False
	plt.figure(figsize=(10, 8), dpi=100)
	plt.figure(1)
	# 输出迭代点
	plt.scatter(x2,'b*',label='迭代点')
	# 输出函数图像
	x = np.linspace(0, 2, 1000)
	f = x ** 3 - 3 * x - 1.2
	plt.plot(x, f, 'r-', label='函数图像')
	plt.title('二分法求根')
	plt.legend(loc=1)
	plt.xlabel('x')
	plt.ylabel('y')
	# 移动坐标轴
	ax = gca()
	ax.spines['top'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position(('test_data', 0))
	ax.spines['left'].set_position(('test_data', 0))
	# 显示
	plt.show()


if __name__ == '__main__':
	x1 = 0
	xn = 2
	err = 10e-5
	f = x ** 3 - 3 * x - 1.2
	qiu_gen(f, x1, xn, err)
