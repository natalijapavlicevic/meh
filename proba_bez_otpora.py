
# * bez otpora vazduha
import matplotlib.pyplot as plt
import numpy as np

g = 9.81
h_init = 10000
# m = 5.24e-7 # masa kapljice

# v(t) - v(0) = -gt

n = 15
t = np.array([(i) for i in range(n)])
v = np.array([(-g*t[i]) for i in range(n)])
h = [h_init]
for i in range(1, n):
    h.append(h[i-1]+t[i]*v[i])

h = np.array(h)

# print(t)
# print(v)
# print(h)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(t, h)
plt.title('Odnos proteklog vremena i visine')

plt.subplot(1, 2, 2)
plt.plot(t, v)
plt.title('Odnos proteklog vremena i brzine')

plt.tight_layout()
plt.show()