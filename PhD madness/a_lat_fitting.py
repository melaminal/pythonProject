import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Load data from the file
data = np.loadtxt('data_a_lat.txt')
x = data[:, 0]
y = data[:, 1]

# Plot the original data
plt.scatter(x, y, color='blue', label='Data Points')

# Perform polynomial fitting
degree = 2  # Degree of the polynomial fit
coefficients = np.polyfit(x, y, degree)
polynomial = np.poly1d(coefficients)

# Generate x values for plotting the fitted curve
x_fit = np.linspace(min(x), max(x), 500)
y_fit = polynomial(x_fit)

# Find the minimum of the fitted polynomial
if degree == 2:
    # For quadratic polynomials, find the vertex analytically
    a, b, c = coefficients
    x_min = -b / (2 * a)
    y_min = polynomial(x_min)
else:
    # For higher-degree polynomials, use numerical methods
    result = minimize_scalar(polynomial)
    x_min = result.x
    y_min = result.fun
print(f'Minimum of fitted polynomial at x = {x_min:.10f}, y = {y_min:.10f}')

# Calculate R-squared value
y_pred = polynomial(x)
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - (ss_res / ss_tot)
print(f'R-squared: {r_squared:.4f}')

# Plot the fitted polynomial curve
plt.plot(x_fit, y_fit, 'r-')
plt.xlabel('a, b lattice constants (Å)', fontsize=14)
plt.ylabel('Energy (eV)', fontsize=14)

# Adjust tick parameters
plt.tick_params(
    axis='both',          # Apply to both axes
    which='both',         # Apply to both major and minor ticks
    direction='in',       # Ticks point inside the plot
    length=8,             # Make ticks longer
    width=1,              # Tick width
    top=True,             # Show ticks on the top axis
    right=True            # Show ticks on the right axis
)

# Optionally adjust tick label font size
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Annotate the minimum point
plt.scatter(x_min, y_min, color='green', s=100, zorder=5, label='Minimum Point')

# Display R-squared and minimum info on the plot
plt.text(0.2, 0.9, f'Minimum: x = {x_min:.10f}, y = {y_min:.10f}\nR-squared: {r_squared:.4f}',
         transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.6), verticalalignment='top')

plt.tight_layout()
plt.show()