from numba import njit
import matplotlib.pyplot as plt
import numpy as np
import time
from PIL import Image


@njit
def Mandelbrot(Re, Im, max_iter=100):
	c = complex(Re, Im)
	z = 0.0j

	for i in range(max_iter):
		z = z*z + c

		if (z.real*z.real + z.imag*z.imag) >= 4:
			return i

	return max_iter

@njit
def BurningShip(Re, Im, max_iter=100):
	c = complex(Re, Im)
	z = 0.0j

	for i in range(max_iter):
		z = (abs(z.real) + 1j*abs(z.imag))**2 + c

		if (z.real*z.real + z.imag*z.imag) >= 4:
			return i

	return max_iter

@njit
def Julia(Re, Im, max_iter=100):
	z = complex(Re, Im)
	c = -1

	for i in range(max_iter):
		z = z*z + c

		if (z.real*z.real + z.imag*z.imag) >= 4:
			return i

	return max_iter


@njit
def Feather(Re, Im, max_iter=100):
	c = complex(Re, Im)
	z = 0.0j

	for i in range(max_iter):
		z = z**3/(1 + z.real*z.real + 1j*z.imag*z.imag) + c

		if (z.real*z.real + z.imag*z.imag) >= 4:
			return i

	return max_iter


@njit
def Custom(Re, Im, step, max_iter=100):
	z = complex(Re, Im)
	r = 0.7885
	c = r*(np.cos(2*np.pi*step) + 1j*np.sin((2*np.pi*step)))

	for i in range(max_iter):
		z = z*z + c

		if (z.real*z.real + z.imag*z.imag) >= 4:
			return i

	return max_iter

DPU = 3

x_range = (-1.7, 1.7)
y_range = (-1.5, 1.5)

x_len = x_range[1] - x_range[0]
y_len = y_range[1] - y_range[0]


rat = x_len/y_len
def_rat = 1920/1080
if rat >= def_rat:
	rows = np.linspace(y_range[0], y_range[1], round(1920/rat)*DPU)
	cols = np.linspace(x_range[0], x_range[1], 1920*DPU)
else:
	rows = np.linspace(y_range[0], y_range[1], 1080*DPU)
	cols = np.linspace(x_range[0], x_range[1], round(1080*rat)*DPU)

res = np.zeros((len(rows), len(cols)))


# steps = np.linspace(0, 1, 1000)

# for i, step in enumerate(steps):
# 	print(i)
# 	for row_id, row in enumerate(rows):
# 		for col_id, col in enumerate(cols):
# 			res[row_id, col_id] = Custom(col, row, step)


# 	fig, ax = plt.subplots(figsize=np.shape(res)[::-1], dpi=1)
# 	# fig, ax = plt.subplots()

# 	fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
# 	ax.imshow(res, cmap="hot", origin="lower")
# 	ax.set_axis_off()
# 	plt.savefig(f"pngs/{i}.png")
# 	plt.close()

for row_id, row in enumerate(rows):
	for col_id, col in enumerate(cols):
		res[row_id, col_id] = BurningShip(col, row)


fig, ax = plt.subplots(figsize=np.shape(res)[::-1], dpi=1)

fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
ax.imshow(res, cmap="hot", origin="lower")
ax.set_axis_off()
plt.savefig(f"julia.png")
plt.close()