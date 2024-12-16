
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from scipy.interpolate import interp1d

# Data
a_lat = [-0.01, -0.005, -0.0025, 0.000, 0.0025, 0.005, 0.01]

datasets = {
    'FM_a0a0c0': [53.343955, -37.50463, -62.998391, -82.142705, -98.620594, -113.270788, -139.040992],
    'G_AFM_a0a0c0': [58.659099, -23.940846, -55.173536, -75.734162, -93.07933, -108.280609, -134.764828],
    'FM_a0a0c_': [111.921171, 92.834436, 76.744813, 53.123107, -21.58616, -62.206429, -104.458198],
    'G_AFM_a0a0c_': [116.553025, 101.070898, 87.503641, 68.541394, 38.516702, -43.42968, -94.194056],
    'FM_a0a0c': [66.792276, 11.650712, -49.882973, -73.182026, -91.692103, -107.680149, -135.039686],
    'G_AFM_a0a0c': [71.249554, 31.629168, -38.951376, -65.486594, -85.300395, -102.037763, -130.330568],
    'FM_a_a_c0': [63.842168, -46.424076, -74.584709, -95.308361, -112.57455, -127.644845, -153.54755],
    'G_AFM_a_a_c0': [72.781471, -26.81284, -63.819338, -86.880692, -105.388247, -121.24793, -148.174896],
    'FM_a_a_c_': [98.614182, 70.884753, 45.186384, -33.255592, -63.651468, -89.732961, -127.958251],
    'G_AFM_a_a_c_': [103.024324, 80.142242, 59.879734, 23.263525, -48.783642, -81.269986, -121.057539]
}

a_lat = [x * 1e2 for x in a_lat]

# Apply transformation to datasets
def transform_data(data):
    return [x ** 2 if x > 0 else x ** 2 * (-1) for x in data]

for key in datasets:
    datasets[key] = transform_data(datasets[key])

# Function to find intersection points
def find_intersections(x, y):
    """Finds coordinates of intersections with y = 0."""
    roots = []
    for i in range(len(x) - 1):
        if y[i] * y[i + 1] < 0:  # Sign change => intersection
            root = x[i] - y[i] * (x[i + 1] - x[i]) / (y[i + 1] - y[i])
            roots.append((root, 0))
    return roots

# Plotting
fig, ax = plt.subplots(figsize=(10, 7), constrained_layout=True)
colors = ['r', 'b', 'g', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
markers = ['o', 's', '^', 'v', 'D', 'h', '*', 'x', 'p', '+']

for i, (key, data) in enumerate(datasets.items()):
    ax.plot(a_lat[:len(data)], data, label=key, color=colors[i % len(colors)], marker=markers[i % len(markers)], markersize=5)

    # Find intersections and plot them
    intersections = find_intersections(a_lat[:len(data)], data)
    print(intersections)
    for x, y in intersections:
        ax.plot(x, y, 'ko', markersize=7)

# Add a horizontal line at y = 0
ax.axhline(0, color='black', linestyle='--', linewidth=1)

# Configure plot
ax.set_xlabel(r'$\mathregular{10^3}$ Misfit strain', fontsize=14)
ax.set_ylabel(r'Frequency squared (cm$^{-2}$)', fontsize=14)
# ax.set_yscale('symlog', linthresh=1e2)
ax.minorticks_on()
ax.tick_params(axis='both', which='both', direction='in', length=8, width=1, top=True, right=True)
ax.tick_params(axis='both', which='minor', length=5, width=1)
legend = ax.legend(loc='upper left')
legend.set_draggable(True)

plt.show()
