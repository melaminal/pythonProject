import matplotlib.pyplot as plt

# Данные
a_lat_cubic = [-0.1, -0.08, -0.06, -0.04, -0.02, -0.01, -0.005, -0.0025,
               0.000, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1]
Energy_cubic = [-176.13861224, -182.96187228, -187.73076959, -190.79619670,
                -192.45563744, -192.83808319, -192.92993438, -192.95247470,
                -192.95985316, -192.95257867, -192.93093282, -192.84608843,
                -192.52011370, -191.31429891, -188.17652082, -184.47362948,
                -180.0]

a_lat_tetragonal = [-0.1, -0.08, -0.06, -0.04, -0.02, -0.01, -0.005, -0.0025,
                    0.000, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1]
Energy_tetragonal = [-189.92190168, -191.17027311, -192.03179338, -192.57914667,
                     -192.87179699, -192.93891976, -192.95460574, -192.95853671,
                     -192.959852, -192.95858789, -192.95488890, -192.94020123,
                     -192.88429051, -192.67697761, -192.36562973, -191.97235611,
                     -191.51477876]

a_lat_tetr_FM_O_rotation = [-0.1, -0.08, -0.06, -0.04, -0.02, -0.01, -0.005, -0.0025,
                            0.000, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1]
Energy_tetr_FM_O_rotation = [-189.92190159, -191.17027297, -192.03222787, -192.58934934,
                             -192.90301893, -192.98382089, -193.00695592, -193.01476125,
                             -193.02007502, -193.02279596, -193.02321415, -193.01684656,
                             -192.97825432, -192.80659744, -192.53042054, -192.17013068,
                             -191.74208233]

a_lat_cubic = [x * 1e2 for x in a_lat_cubic]
a_lat_tetragonal = [x * 1e2 for x in a_lat_tetragonal]
a_lat_tetr_FM_O_rotation = [x * 1e2 for x in a_lat_tetr_FM_O_rotation]

plt.figure(figsize=(4, 6))  # 4x6 дюймов

plt.plot(a_lat_cubic, Energy_cubic, 'r-', marker='o', markersize=5, label='Cubic')
plt.plot(a_lat_tetragonal, Energy_tetragonal, 'b-', marker='s', markersize=5, label='Tetragonal')
plt.plot(a_lat_tetr_FM_O_rotation, Energy_tetr_FM_O_rotation, 'g-', marker='p', markersize=5,
         label='Tetragonal_O_rotated')

plt.xlabel(r'$\mathregular{10^3}$ Misfit strain', fontsize=14)
plt.ylabel('Energy (eV)', fontsize=14)

plt.minorticks_on()

plt.tick_params(
    axis='both',
    which='both',
    direction='in',
    length=8,
    width=1,
    top=True,
    right=True
)

plt.tick_params(
    axis='both',
    which='minor',
    direction='in',
    length=5,
    width=1,
    top=True,
    right=True
)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add draggable legend
legend = plt.legend(loc='upper left')
legend.set_draggable(True)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show(block=True)