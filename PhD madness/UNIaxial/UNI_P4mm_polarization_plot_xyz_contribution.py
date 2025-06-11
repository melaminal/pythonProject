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
    "strain": [0.0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5],  # Примерные значения, замени на реальные
    "ionic_x": [0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
    "electronic_x": [3.88763, 3.87503, 7.73411, 3.85918, -0.00003, -0.00004, -3.83620, -0.00006, -3.82112, -7.62714,
                     -3.80611],
    "ionic_y": [0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000, 0.00000],
    "electronic_y": [3.88763, 3.87505, 0.00004, 3.85924, 0.00005, 0.00005, 3.83621, 0.00006, -3.82100, 0.00006,
                     3.80611],
    "ionic_z": [28.69150, 0.00227, -2.24806, -4.02714, -5.58953, -7.02537, -8.36122, -9.62098,
                -10.81540, -11.95221, -13.04231],
    "electronic_z": [-1.47376, -7.39278, -6.94375, -6.49886, -6.05387, -5.60694, -5.16597,
                     -4.73049, -4.29429, -3.87452, -3.46048],
    "a": [3.887626363, 3.875030526, 3.867056867, 3.859193298, 3.851431120, 3.843767485, 3.836151444, 3.828578693,
          3.821056509, 3.813535902, 3.806046760],
    "c": [7.778997835, 7.895682802, 7.973472780, 8.051262759, 8.129052737, 8.206842715, 8.284632694, 8.362422672,
          8.440212650, 8.518002629, 8.595792607],
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
    "ionic_z":      4,
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
    "ionic_z":      (-35,  35),
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
fig, axs = plt.subplots(2, 3, figsize=(13, 7))
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
        ax.set_xlabel("Biaxial Strain (%)")
        ax.set_ylabel("Dip. mom. (eÅ)")

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