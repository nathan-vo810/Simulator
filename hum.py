import numpy as np
from sklearn.preprocessing import normalize


y = np.arange(1,7).reshape(2,3)
print(y)
norm2 = normalize(y, axis=0)
print(norm2)

z = normalize(np.array([[0.9, 1700, 100]]),axis=0)
print(z)