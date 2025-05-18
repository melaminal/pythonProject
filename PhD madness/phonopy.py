import yaml
import numpy as np
import matplotlib.pyplot as plt

with open("/home/dieguez/Downloads/programs/vasp6/phonopy/EuTiO3_5_atoms/band.yaml") as f:
    data = yaml.safe_load(f)

phonons = data["phonon"]
distances = np.array([p["distance"] for p in phonons])
frequencies = np.array([[b["frequency"] for b in p["band"]] for p in phonons])

# --- задаём метки вручную
labels = ['Γ', 'X', 'M', 'Γ', 'R', 'X', 'M', 'R']
n_segments = len(labels) - 1
points_per_segment = (len(distances) - 1) // n_segments
tick_positions = [i * points_per_segment for i in range(len(labels))]

# --- график
fig, ax = plt.subplots(figsize=(6, 4))

for branch in frequencies.T:
    ax.plot(distances, branch.ravel(), color="black", linewidth=0.7)

# горизонтальная линия по нулю
ax.axhline(0, color="gray", linestyle=":", linewidth=0.7)

# подписи оси X
ax.set_xticks([distances[i] for i in tick_positions])
ax.set_xticklabels(labels)

ax.set_ylabel(r"Wavenumber (cm$^{-1}$)")
ax.set_xlim(distances[0], distances[-1])
ax.set_ylim(-200, 850)

plt.tight_layout()
plt.show()