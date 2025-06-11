import yaml, numpy as np, matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter      # <<<

with open("/home/dieguez/Downloads/programs/vasp6/phonopy/EuTiO3_5_atoms_strained_5%/band.yaml") as f:
    data = yaml.safe_load(f)

phonons     = data["phonon"]
distances   = np.array([p["distance"]           for p in phonons])
frequencies = np.array([[b["frequency"] for b in p["band"]]
                        for p in phonons])

labels = ['Γ', 'X', 'M', 'Γ', 'R', 'X', 'M', 'R']
boundaries = np.where(np.diff(distances) < 1e-8)[0] + 1
segments   = np.split(np.arange(len(distances)), boundaries)

fig, ax = plt.subplots(figsize=(6, 4))

for branch in frequencies.T:
    for seg in segments:
        ax.plot(distances[seg], branch[seg], color='black', lw=0.7)

ax.axhline(0, color='gray', ls=':', lw=0.7)

# k-точки
tick_pos = [distances[s[0]] for s in segments] + [distances[segments[-1][-1]]]
ax.set_xticks(tick_pos)
ax.set_xticklabels(labels)

# ── кастомный форматтер оси y ──────────────────────────────────
def yfmt(y, _):
    if np.isclose(y, -200):      # именно -200 → показать «200 i»
        return r'$200\,i$'
    elif np.isclose(y, -300):
        return r'$300\,i$'
    else:                        # положительные остаются целыми
        return f'{int(y)}'

ax.set_ylim(-300, 850)
ax.yaxis.set_major_formatter(FuncFormatter(yfmt))   # <<<

ax.set_ylabel(r'Wavenumber (cm$^{-1}$)')

ax.margins(x=0)      # убирает стандартные 5 % отступа по оси X
plt.tight_layout()
plt.show()
