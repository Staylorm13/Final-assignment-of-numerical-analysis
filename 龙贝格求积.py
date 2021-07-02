import numpy as np


def func(x):
    return np.sin(x)


class Romberg(object):
    def __init__(self, a, b, sigma):
        self.a = a  # 下限
        self.b = b  # 上限
        self.sigma = sigma  # 误差限

    def calc(self):
        a = self.a
        b = self.b
        sigma = self.sigma
        k = 1
        i = 0

        Tn = []
        Sn = []
        Cn = []
        Rn = []

        # 循环生成hm间距序列
        hm = [(b - a) / (2 ** i) for i in range(0, 5)]
        print('hm的取值：', hm)

        # 循环生成Tn
        fa = func(a)
        fb = func(b)

        T0 = round((1 / 2) * (b - a) * (fa + fb), 6)  # round函数用于设置精度，精度为6
        Tn.append(T0)

        while k > sigma and i < 5:
            i += 1
            sum = 0
            # 多出来的点的累加和
            for j in range(1, 2 ** i, 2):
                sum = sum + hm[i] * func(a + j * hm[i])  # 计算两项值
            Tn.append(round(sum + (1 / 2) * Tn[i - 1], 6))
            Sn.append(round((4 * Tn[i] - Tn[i - 1]) / 3, 6))
            k = abs(Sn[0] - Tn[0])
            if i > 1:
                Cn.append(round((16 * Sn[i - 1] - Sn[i - 2]) / 15, 6))
                k = abs(Cn[0] - Sn[0])
                if i > 2:
                    Rn.append(round((64 * Cn[i - 2] - Cn[i - 3]) / 63, 6))
                    k = abs(Rn[0] - Cn[0])

        f = Rn[-1]
        print('T序列：', Tn)
        print('S序列：', Sn)
        print('C序列：', Cn)
        print('R序列：', Rn)
        print('积分值：', f)
        print('截断误差：', k)


if __name__ == '__main__':
    rom = Romberg(1, 2, 0.00001)
    rom.calc()
