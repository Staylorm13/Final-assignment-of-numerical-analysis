from numpy import zeros, array, concatenate


class ClassGauss(object):
	
	def __init__(self, A, b):
		super(ClassGauss, self).__init__()
		self.A = A
		self.b = b
		self.m = len(b)
		self.n = len(b[0])
	
	def gauss(self):
		A = self.A
		b = self.b
		m = self.m
		n = self.n
		X = zeros((m, n))
		for i in range(0, m - 1):  # 从0开始计
			print('A的变换可视化\n', concatenate((A, b), axis=1), '\n')
			print(i + 1)
			mi = i
			for j in range(i, m):
				if abs(A[mi, i]) < abs(A[j, i]):  # 找每列中最大元素
					mi = j
			if mi != i:
				for k in range(i, m):
					A[i, k], A[mi, k] = A[mi, k], A[i, k]  # A中i行与j行互换
				for k in range(0, n):  # 从0开始计
					b[i, k], b[mi, k] = b[mi, k], b[i, k]  # b中i行与j行互换
				print('%d-1\n' % (i + 1), concatenate((A, b), axis=1), '\n')
			for j in range(1, m - i):
				a, A[i + j, i] = A[i + j, i], 0
				for k in range(i + 1, m):
					A[i + j, k] = A[i + j, k] - A[i, k] * a / A[i, i]  # A消元：主元下元素化为0
				for k in range(0, n):
					b[i + j, k] = b[i + j, k] - b[i, k] * a / A[i, i]  # b消元：主元下元素化为0
				print('%d-2\n' % (i + 1), concatenate((A, b), axis=1), '\n')
		
		for i in range(0, n):  # 求X的值
			X[m - 1, i] = b[m - 1, i] / A[m - 1, m - 1]
			for j in range(m - 2, -1, -1):  # 倒数则顺序为-1，起点-1，若要记到0，则终点为-1
				y = b[j, i]
				for k in range(m - 1, j, -1):
					y = y - A[j, k] * X[k, i]
				X[j, i] = y / A[j, j]
		return A, b, X


if __name__ == '__main__':
	A = array([[12, -3, 3], [-18, 3, -1], [1, 1, 1]], dtype=float)
	b = array([[15], [-15], [6]], dtype=float)
	# A = array([[-2,0,1,0,0,0], [-2,0,0,1,0,0], [-1,0,0,0,1,0],[0.6,1,0,0,0,1],[-5,0,0,0,0,0]], dtype=float)
	# b = array([[-200], [800], [500], [600], [0]], dtype=float)
	
	g = ClassGauss(A, b)
	A, b, X = g.gauss()
	print('A=\n', A)
	print('b=\n', b)
	print('X=\n', X)
