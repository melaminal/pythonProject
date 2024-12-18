import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import brentq
import matplotlib.pyplot as plt

# Define the data
CONTCAR_00025 = [3.899083345834324, 3.9384680260952765, 3.977852706356229]
sigma_33_00025 = [41.53911, -2.34575, -41.34627]

CONTCAR_0005 = [3.8968523599789266, 3.936214505029219, 3.9755766500795113]
sigma_33_0005 = [41.44344, -2.61826, -41.47652]

CONTCAR_001 = [3.892230030597988, 3.931545485452513, 3.9708609403070385]
sigma_33_001 = [41.64915, -2.52214, -41.44889]

CONTCAR_002 = [3.8829735120055404, 3.922195466672263, 3.9614174213389854]
sigma_33_002 = [42.47530, -2.10505, -41.26311]

CONTCAR_004 = [3.8668062626341526, 3.9058649117516695, 3.9449235608691864]
sigma_33_004 = [42.43982, -2.63025, -42.16847]

CONTCAR_006 = [3.8515015590065998, 3.8904056151581816, 3.9293096713097633]
sigma_33_006 = [42.92605, -2.47662, -42.73665]

CONTCAR_008 = [3.8367099719187787, 3.8754646180997763, 3.914219264280774]
sigma_33_008 = [44.56537, -1.66623, -42.35606]

CONTCAR_01 = [3.822547365015089, 3.861158954560696, 3.899770544106303]
sigma_33_01 = [46.77923, -0.01899, -41.31130]

# Line x and y
x = [3.8, 4.0]
y = [0.00602, 0.00602]

dataSets = [
    np.array(CONTCAR_00025), np.array(CONTCAR_0005), np.array(CONTCAR_001),
    np.array(CONTCAR_002), np.array(CONTCAR_004), np.array(CONTCAR_006),
    np.array(CONTCAR_008), np.array(CONTCAR_01),
]

sigmaSets = [
    np.array(sigma_33_00025), np.array(sigma_33_0005), np.array(sigma_33_001),
    np.array(sigma_33_002), np.array(sigma_33_004), np.array(sigma_33_006),
    np.array(sigma_33_008), np.array(sigma_33_01),
]

names = [
    'sigma_33_00025', 'sigma_33_0005', 'sigma_33_001',
    'sigma_33_002', 'sigma_33_004', 'sigma_33_006',
    'sigma_33_008', 'sigma_33_01',
]

all_CONTCAR_values = np.concatenate(dataSets)
min_x = np.min(all_CONTCAR_values) - 0.5
max_x = np.max(all_CONTCAR_values) + 0.5
commonX = np.linspace(min_x, max_x, 5000)

interp_func_line = interp1d(x, y, kind='linear', fill_value='extrapolate')
interpY_line = interp_func_line(commonX)

intersections = {name: [] for name in names}

for i, (data, sigma, name) in enumerate(zip(dataSets, sigmaSets, names)):
    interp_func_i = interp1d(data, sigma, kind='linear', fill_value='extrapolate')
    interpY_data = interp_func_i(commonX)
    diff = interpY_line - interpY_data
    idx = np.where(diff[:-1] * diff[1:] <= 0)[0]

    for j in idx:
        x0, x1 = commonX[j], commonX[j + 1]
        f0 = interp_func_line(x0) - interp_func_i(x0)
        f1 = interp_func_line(x1) - interp_func_i(x1)
        if f0 * f1 > 0:
            continue
        try:
            x_cross = brentq(lambda xq: interp_func_line(xq) - interp_func_i(xq), x0, x1)
            y_cross = interp_func_line(x_cross)
            intersections[name].append([f'{x_cross:.17f}', f'{y_cross:.5f}'])
        except ValueError:
            continue

for key, value in intersections.items():
    print(f"{key}: {value}")

plt.figure()
for data, sigma, name in zip(dataSets, sigmaSets, names):
    plt.plot(data, sigma, '-o', label=name)
plt.plot(x, y, '-', color='k', label='Reference Line')

for name in names:
    for point in intersections[name]:
        plt.plot(float(point[0]), float(point[1]), '*', color='red', markersize=8)

plt.xlabel('Lattice parameter c (Å)', fontsize=14)
plt.ylabel('σ₃₃ (kbar)', fontsize=14)
plt.grid(True)
plt.show()