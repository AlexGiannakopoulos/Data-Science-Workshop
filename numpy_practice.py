import numpy as np

a = np.random.randint(1, 100, size=(5, 5))

print(a)

print(np.extract(a[2:5], arr= a))
