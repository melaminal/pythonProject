
import matplotlib.pyplot as plt

a_lat = [0.000, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1]
FM_a0a0c0 = [-192.95985316, -192.95858787, -192.95488885, -192.94020107, -192.88429090,
             -192.67697727, -192.36563019, -191.97235501, -191.51477876]
FM_a0a0c_ = [-193.02007531, -193.02279628, -193.02321433, -193.01684648, -192.97825321,
             -192.80660013, -192.53042156, -192.17012857, -191.74208239]
FM_a0a0c = [-192.96149223, -192.96135909, -192.95906595, -192.94787222, -192.90167874,
            -192.72183192, -192.44441824, -192.08759706, -191.66611335]
FM_a_a_c0 = [-193.0252993, -193.0207191, -193.0139306, -192.9936183, -192.9283315,
             -192.7086370, -192.4415655, -192.0813036, -191.6613220]
FM_a_a_c = [-193.0252747, -193.0207000, -193.0139163, -192.9936074, -192.9283885,
            -192.7281495, -192.4444130, -192.0863695, -191.6653571]
FM_a_a_c_ = [-193.0241273, -193.0242852, -193.0234939, -193.0166564, -192.9782414,
             -192.8065982, -192.5304200, -192.1701290, -191.7420816]

# Convert a_lat to a larger scale
a_lat = [x * 1e2 for x in a_lat]

# Plotting
fig, ax = plt.subplots()
ax.plot(a_lat, FM_a0a0c0, marker='o', label='FM_a0a0c0')
ax.plot(a_lat, FM_a0a0c_, marker='s', label='FM_a0a0c_')
ax.plot(a_lat, FM_a0a0c, marker='^', label='FM_a0a0c')
ax.plot(a_lat, FM_a_a_c0, marker='d', label='FM_a_a_c0')
ax.plot(a_lat, FM_a_a_c, marker='v', label='FM_a_a_c')
ax.plot(a_lat, FM_a_a_c_, marker='v', label='FM_a_a_c_')

# Axis labels
ax.set_xlabel(r'$\mathregular{10^2}$ Misfit strain', fontsize=14)
ax.set_ylabel('Energy (eV)', fontsize=14)

# Grid and ticks
ax.minorticks_on()
ax.tick_params(axis='both', which='both', direction='in', length=8, width=1, top=True, right=True)
ax.tick_params(axis='both', which='minor', direction='in', length=5, width=1, top=True, right=True)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Legend
legend = ax.legend(loc='upper left')
legend.set_draggable(True)

# Layout optimization and display
plt.tight_layout()
plt.show()
