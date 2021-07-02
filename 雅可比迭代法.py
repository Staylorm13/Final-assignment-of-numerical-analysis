import numpy as np


def Jacobi(A, b, x0, err):
	n = 0
	m = len(x0)
	B = np.zeros((m, m), 'f')
	tr = np.zeros(m, 'f')
	for i in range(0, m):
		for j in range(0, m):
			if i != j:
				B[i, j] = A[i, j]
			else:
				tr[i] = A[i, j]
	x1 = np.divide((b - np.matmul(B, x0)), tr)
	while max(abs(x1 - x0)) > err:
		n = n + 1
		x0 = x1
		for i in range(0, m):
			for j in range(0, m):
				if i != j:
					B[i, j] = A[i, j]
				else:
					tr[i] = A[i, j]
		x1 = np.divide((b - np.matmul(B, x0)), tr)
	n = n + 1
	print('在经过%d次迭代后，求得收敛点为：\n' % n, x1)


A = np.array([[8, 2, 3, 4], [2, 13, 6, 4], [2, 4, 12, 5], [3, 2, 4, 9]])
b = np.array([2.74, 2.76, 2.89, 2.79])
x0 = np.zeros(4, 'f')
Jacobi(A, b, x0, 10e-5)
