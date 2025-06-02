import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array ([[1, 2, 5], [3, 4, 78]])
c = np.array([1, 2, 3])
d = np.array([[1, 2, 3], [4, 5, 6]])
e = np.array([10, 15, 20, 25])
mask = e > 15
f = np.array([3, 7 , 12, 18])

g1 = np.zeros((2, 3)) # 2x3 matrix of 0s
g2 = np.ones((3, 3))        # 3x3 matrix of 1s
g3 = np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
g4 = np.linspace(0, 1, 5)   # 5 evenly spaced numbers from 0 to 1
g5 = np.random.rand(2, 2)   # random values between 0 and 1


# print(a[1])
# print(a[1:3])
# print(b[0,2])
# print(b[1, :])
# print(b[:, 1]) # pairnei thn sthlh oxi th grammh

# print(c + 5)
# print(c * 2)
# print(np.sqrt(c))
# print((a-5)**2)

# print(d.sum())
# print(d.mean())
# print(d.sum(axis=0))
# print(d.sum(axis=1))

# print(mask)
# print(e[mask])
# print(e[e > 15])
# print(f[f > 10])

print(g1)
print(g2)
print(g3)
print(g4)
print(g5)