import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

mat = loadmat('Pyecltest_angle3D_ref.mat')

matkeys = list(mat.keys())

print(matkeys)

matkeys.remove('__header__')
matkeys.remove('__version__')
matkeys.remove('__globals__')

for key in matkeys:
    print('Parametro:', key)
    print('Tamaño:', mat[key].shape)
    print('Tipo:', mat[key].dtype)

x = mat['t'].flatten()
y = mat['Nel_timep'].flatten()

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111)

ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Num. de electrones')

ax.plot(x,y)

plt.plot()
plt.show()

#plt.scatter(mat['t'], mat['cen_density'])

#plt.show()

