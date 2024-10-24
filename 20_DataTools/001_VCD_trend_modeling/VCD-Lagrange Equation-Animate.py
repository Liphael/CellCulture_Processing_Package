# 导入包
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# 规定{x}
n = 15
x = sp.symbols("x")

# 生成{x}数列
A = np.arange(n,dtype = np.float64)
Y = np.array([0.835,1.29,2.8,6.09,8.69,10.8,13.4,15.3,17.8,17.4,16,15.1,15.5,13.4,13.1],dtype = np.float64)

# 计算L(x)
RES = 0
i = int(0)
for A[i] in A:
    B = np.delete(A,[i])
    LxDen = float(1)
    LxNum = float(1)
    ii = int(0)
    for B[ii] in B:
        LxDen = LxDen * (A[i] - B[ii])
        ii = ii + 1
    ii = int(0)
    for B[ii] in B:
        LxNum = LxNum * (x - B[ii])
        ii = ii + 1
    Lx = LxNum / LxDen
    RES = RES + Y[i] * Lx
    i = i + 1
RES = sp.simplify(RES)

# 生成点
Xa = np.linspace(0, 14, 500)
Ya = np.array([],dtype = np.float64)
i = int(0)
for Xa[i] in Xa:
    Yi = np.array([RES.subs(x, Xa[i])])
    Ya = np.concatenate((Ya, Yi), axis = None)
    i = i + 1

# 绘制
plt.plot(Xa, Ya, color = 'blue', linewidth = 0.5, linestyle = '-')
plt.title('∑ yL(x)')
plt.xlabel('x(/days)')
plt.ylabel('VCD(/10^6 cells)')
plt.xlim(0,14)
plt.ylim(0,20)

plt.show()