import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(9)
def line_gen(D,C):
  len =10
  dim = D.shape[0]
  x_DC = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = D + lam_1[i]*(C-D)
    x_DC[:,i]= temp1.T
  return x_DC

A = np.array([-2.83,1])
B = np.array([2.83,1])
C = np.array([2.83,-1])
D = np.array([-2.83,-1])

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)
x_DC = line_gen(D,C)
x_CB = line_gen(C,B)
x_BA = line_gen(B,A)
x_AD = line_gen(A,D)
x_DB = line_gen(D,B)
x_CA = line_gen(C,A)

fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)

plt.xlim(-3,3)
plt.ylim(-3,3)

plt.grid(linestyle='--')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(x_CB[0,:],x_CB[1,:],label='$CB$')
plt.plot(x_BA[0,:],x_BA[1,:],label='$BA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_DB[0,:],x_DB[1,:],label='$DB$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.2), D[1] * (1) , 'D')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.03), B[1] * (1 - 0.1), 'B')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')

plt.show()