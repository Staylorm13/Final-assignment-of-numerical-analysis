import numpy as np


def mi_fa(A, v0, error):
	# A = np.asarray(A)
	# v0 = np.asarray(v0)
	er = 1.0
	u0 = v0
	while error < er:
		miu0 = max(v0)
		v0 = np.matmul(A, u0)
		miu1 = max(v0)
		u0 = np.divide(v0, miu1)
		er = abs(miu0 - miu1)
	else:
		print('主特征值：', miu1)
		print('主特征向量：', u0)


if __name__ == '__main__':
	A = np.array([[0, 0, 0], [0.5, 1, 0], [0, 0.5, 1]])
	v0 = np.array([0, 1, 1.5])
	error = 1.0e-4
	mi_fa(A, v0, error)
