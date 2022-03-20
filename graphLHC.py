import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

rect11 = loadmat('P1-sey1.1-SecRecta.mat')
dipo11 = loadmat('P1-sey1.1-Dipolo.mat')
cuad11 = loadmat('P1-sey1.1-Cuadrupolo.mat')

rect12 = loadmat('P1-sey1.2-SecRecta.mat')
dipo12 = loadmat('P1-sey1.2-Dipolo.mat')
cuad12 = loadmat('P1-sey1.2-Cuadripolo.mat')

rect13 = loadmat('P1-sey1.3-SecRecta.mat')
dipo13 = loadmat('P1-sey1.3-Dipolo.mat')
cuad13 = loadmat('P1-sey1.3-Cuadrupolo.mat')

rect14 = loadmat('P1-sey1.4-SecRecta.mat')
dipo14 = loadmat('P1-sey1.4-Dipolo.mat')
cuad14 = loadmat('P1-sey1.4-Cuadrupolo.mat')

rect15 = loadmat('sey1.5_rect_Pyecltest_angle3D.mat')
dipo15 = loadmat('sey1.5_dip_Pyecltest_angle3D.mat')
cuad15 = loadmat('sey1.5_cuadrup_Pyecltest_angle3D.mat')

rect16 = loadmat('P1-sey1.6-SecRecta.mat')
dipo16 = loadmat('P1-sey1.6-Dipolo.mat')
cuad16 = loadmat('P1-sey1.6-Cuadrupolo.mat')

rect11X = rect11['t'].flatten()
rect11Y = rect11['Nel_timep'].flatten()
dipo11X = dipo11['t'].flatten()
dipo11Y = dipo11['Nel_timep'].flatten()
cuad11X = cuad11['t'].flatten()
cuad11Y = cuad11['Nel_timep'].flatten()

rect12X = rect12['t'].flatten()
rect12Y = rect12['Nel_timep'].flatten()
dipo12X = dipo12['t'].flatten()
dipo12Y = dipo12['Nel_timep'].flatten()
cuad12X = cuad12['t'].flatten()
cuad12Y = cuad12['Nel_timep'].flatten()

rect13X = rect13['t'].flatten()
rect13Y = rect13['Nel_timep'].flatten()
dipo13X = dipo13['t'].flatten()
dipo13Y = dipo13['Nel_timep'].flatten()
cuad13X = cuad13['t'].flatten()
cuad13Y = cuad13['Nel_timep'].flatten()

rect14X = rect14['t'].flatten()
rect14Y = rect14['Nel_timep'].flatten()
dipo14X = dipo14['t'].flatten()
dipo14Y = dipo14['Nel_timep'].flatten()
cuad14X = cuad14['t'].flatten()
cuad14Y = cuad14['Nel_timep'].flatten()

rect15X = rect15['t'].flatten()
rect15Y = rect15['Nel_timep'].flatten()
dipo15X = dipo15['t'].flatten()
dipo15Y = dipo15['Nel_timep'].flatten()
cuad15X = cuad15['t'].flatten()
cuad15Y = cuad15['Nel_timep'].flatten()

rect16X = rect16['t'].flatten()
rect16Y = rect16['Nel_timep'].flatten()
dipo16X = dipo16['t'].flatten()
dipo16Y = dipo16['Nel_timep'].flatten()
cuad16X = cuad16['t'].flatten()
cuad16Y = cuad16['Nel_timep'].flatten()

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111)

ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Num. de electrones')

#ax.plot(x,y)

plt.title("Sección recta")

ax.plot(rect11X, rect11Y, label='SEY 1.1')
ax.plot(rect12X, rect12Y, label='SEY 1.2')
ax.plot(rect13X, rect13Y, label='SEY 1.3')
ax.plot(rect14X, rect14Y, label='SEY 1.4')
ax.plot(rect15X, rect15Y, label='SEY 1.5')
ax.plot(rect16X, rect16Y, label='SEY 1.6')

plt.legend()

plt.plot()
plt.show()

#------------------------------------------------#

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111)

ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Num. de electrones')

#ax.plot(x,y)

plt.title("Dipolo")

ax.plot(dipo11X, dipo11Y, label='SEY 1.1')
ax.plot(dipo12X, dipo12Y, label='SEY 1.2')
ax.plot(dipo13X, dipo13Y, label='SEY 1.3')
ax.plot(dipo14X, dipo14Y, label='SEY 1.4')
ax.plot(dipo15X, dipo15Y, label='SEY 1.5')
ax.plot(dipo16X, dipo16Y, label='SEY 1.6')

plt.legend()

plt.plot()
plt.show()

#------------------------------------------------#

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111)

ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Num. de electrones')

#ax.plot(x,y)

plt.title("Cuadrupolo")

ax.plot(cuad11X, cuad11Y, label='SEY 1.1')
ax.plot(cuad12X, cuad12Y, label='SEY 1.2')
ax.plot(cuad13X, cuad13Y, label='SEY 1.3')
ax.plot(cuad14X, cuad14Y, label='SEY 1.4')
ax.plot(cuad15X, cuad15Y, label='SEY 1.5')
ax.plot(cuad16X, cuad16Y, label='SEY 1.6')

plt.legend()

plt.plot()
plt.show()

