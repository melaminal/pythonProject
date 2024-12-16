import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import brentq
import matplotlib.pyplot as plt

# Define the data
CONTCAR_00025 = [3.8202555052132006, 3.8990236599598647, 3.9777918147065283, 4.056559969453192]
sigma_33_00025 = [147.03326, 41.46958, -41.33079, -105.82313]

CONTCAR_0005 = [3.8202555052132006, 3.8990236599598647, 3.9777918147065283, 4.056559969453192]
sigma_33_0005 = [143.71348, 38.86303, -43.43397, -107.34949]

CONTCAR_001 = [3.8202555052132006, 3.8990236599598647, 3.9777918147065283, 4.056559969453192]
sigma_33_001 = [137.64334, 33.69575, -47.90108, -111.03132]

CONTCAR_002 = [3.8202555052132006, 3.8990236599598647, 3.9777918147065283, 4.056559969453192]
sigma_33_002 = [125.61708, 23.55454, -56.49418, -118.00742]

CONTCAR_004 = [3.7808714278398687, 3.8596395825865324, 3.9384077373331965, 4.017175892079861]
sigma_33_004 = [162.87367, 51.18911, -36.02709, -103.49164]

CONTCAR_006 = [3.7808714278398683, 3.8596395825865324, 3.9384077373331965]
sigma_33_006 = [141.21974, 32.94662, -51.38893]

CONTCAR_008 = [3.78087142783986, 3.85963958258653, 3.93840773733319]
sigma_33_008 = [121.86214, 16.41868, -65.27434]

CONTCAR_01 = [3.74148735046653, 3.7808714278398687, 3.8202555052132006, 3.859639582586533, 3.8990236599598647]
sigma_33_01 = [165.61976, 104.13563, 49.65945, 1.63244, -40.52646]

# Line x and y
x = [3.7, 4.1]
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