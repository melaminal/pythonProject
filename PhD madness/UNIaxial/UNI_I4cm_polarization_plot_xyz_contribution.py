import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl

mpl.rcParams.update({
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
    "xtick.major.size": 9,
    "ytick.major.size": 9,
    "xtick.minor.size": 4,
    "ytick.minor.size": 4,
    "xtick.major.width": 1,
    "ytick.major.width": 1,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
})

# Данные вручную переписаны из изображения
data = {
    "strain": [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],  # Примерные значения, замени на реальные
    "ionic_x": [0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
    "electronic_x": [-7.74398, 7.72089, 7.69839, -3.83884, -3.83061, 3.82254, 7.62917, -7.61415, -7.60070, 0.00002,
                     3.80972],
    "ionic_y": [0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
    "electronic_y": [-0.00034, -0.00033, -0.00033, -3.83922, -3.83094, 3.82226, -0.00018, -0.00014, -0.00012, -0.00008,
                     3.80985],
    "ionic_z": [0.96530, 0.97326, 0.98290, -0.35780, -2.14886, -3.38437, -4.52373, -5.69163, -7.00483, -8.70309,
                -15.82384],
    "electronic_z": [-4.85503, -4.90098, -4.94949, -5.35325, -5.64262, -5.64361, -5.50673, -5.25125, -4.84049,
                     -4.17279, -0.34585],
    "a": [3.872026743, 3.860410690, 3.849164869, 3.838901047, 3.830667580, 3.822486229, 3.814559499, 3.807094446,
          3.800368168, 3.795280706, 3.809785059],
    "c": [7.778997835, 7.856787813, 7.934577791, 8.012367770, 8.090157748, 8.167947726, 8.245737705, 8.323527683,
          8.401317661, 8.479107640, 8.556897618],
}

df = pd.DataFrame(data)

# ───────────────────── 2. КВАНТЫ ПОЛЯРИЗАЦИИ ───────────────────
q_x = q_y = df["a"].mean()
q_z = df["c"].mean()
quanta = {"x": q_x, "y": q_y, "z": q_z}
print(quanta)

# ────────────────── 3. КОЛИЧЕСТВО ЛИНИЙ («веток») ──────────────
BRANCHES = {
    "electronic_x": 4,      #  −2 … +2
    "electronic_y": 3,      #  −1 … +3
    "electronic_z": 2,      #  только реальные данные
    "ionic_x":      2,
    "ionic_y":      2,
    "ionic_z":      2,
}
DEFAULT_BRANCHES = 1        # если ключ не указан

def n_iter(key: str):
    setting = BRANCHES.get(key, DEFAULT_BRANCHES)
    if isinstance(setting, int):
        return range(-setting, setting + 1)
    down, up = setting
    return range(-down, up + 1)

# ────────────────── 4. ДИАПАЗОНЫ ПО Y (min, max) ───────────────
# None ⇒ автоматический выбор; иначе вручную
YRANGE = {
    "electronic_x": (-10,  10),
    "electronic_y": (-10,  10),
    "electronic_z": (-20,  20),
    "ionic_x":      (-15,  15),
    "ionic_y":      (-15,  15),
    "ionic_z":      (-30,  30),
}
DEFAULT_YRANGE = None       # авто, если ключ не указан

def set_ylim(ax, key):
    yr = YRANGE.get(key, DEFAULT_YRANGE)
    if yr is not None:
        ax.set_ylim(*yr)

def make_coord_formatter(ndigits=2):
    """Возвращает функцию, печатающую x,y с заданной точностью."""
    return lambda x, y: f"x = {x:.{ndigits}f},   y = {y:.{ndigits}f}"

# ─────────────────────────── 5. ГРАФИК ─────────────────────────
fig, axs = plt.subplots(2, 3, figsize=(11, 7))
axes  = ["x", "y", "z"]
parts = ["electronic", "ionic"]

for ax in axs.flat:                # axs.flat обходит все 6 Axes
    ax.format_coord = make_coord_formatter(5)   # ← здесь задаём .2f

for row, part in enumerate(parts):
    for col, axis in enumerate(axes):
        ax   = axs[row, col]
        q    = quanta[axis]
        key  = f"{part}_{axis}"
        n_rg = n_iter(key)

        ax.set_title(f"{part.capitalize()} {axis}")
        ax.set_xlabel("Biaxial Strain (%)",  fontsize=14)
        if col == 0:
            ax.set_ylabel("Dip. mom. (eÅ)", fontsize=14)

        # пустые ветки
        for n in (k for k in n_rg if k != 0):
            ax.plot(df["strain"],
                    df[key] + n * q,
                    marker='o', linestyle='none', markersize=8,
                    mfc='none', mec='purple', zorder=1)

        # реальные данные
        ax.plot(df["strain"],
                df[key],
                marker='o', linestyle='none', markersize=8,
                mfc='purple', mec='purple', zorder=2)

        ax.axhline(0, color='k', lw=0.6)
        set_ylim(ax, key)   # ← применяем индивидуальный диапазон

from matplotlib.ticker import AutoMinorLocator

for ax in axs.flat:
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

plt.tight_layout()
plt.show()