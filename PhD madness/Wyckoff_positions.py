from pymatgen.io.cif import CifParser
from pymatgen.core import Element
from collections import Counter

# === Параметры ===
file1 = "POSCAR_Pm3m_SrTiO3.cif"
file2 = "POSCAR_Pnma_SrTiO3.cif"
output_file = "comsubs.in"

# === Загрузка и расширение первой структуры (Pm-3m) ===
s1 = CifParser(file1).get_structures()[0]
s1_super = s1 * [2, 2, 1]  # Получаем 20 атомов

# === Загрузка второй структуры (Pnma) ===
s2 = CifParser(file2).get_structures()[0]

# === Упорядочим атомы по типу и координатам ===
def sorted_sites(structure):
    return sorted(structure.sites, key=lambda site: (Element(site.species_string).number, *site.frac_coords))

# === Группировка и сортировка по типу ===
def reorder_by_type(structure):
    sites = sorted_sites(structure)
    type_order = ['Sr', 'Ti', 'O']
    grouped = []
    for t in type_order:
        grouped.extend([site for site in sites if site.species_string == t])
    return grouped

# === Генерация блока для comsubs ===
def structure_block(structure, spg_number):
    lines = [f"{spg_number} ! space group symmetry of crystal"]
    a, b, c, alpha, beta, gamma = structure.lattice.parameters
    lines.append(f"{a:.6f} {b:.6f} {c:.6f} {alpha:.6f} {beta:.6f} {gamma:.6f} ! lattice parameters")
    sites = reorder_by_type(structure)
    lines.append(f"{len(sites)} ! number of Wyckoff positions")
    for site in sites:
        element = site.species_string
        x, y, z = site.frac_coords
        lines.append(f"{element} {x:.6f} {y:.6f} {z:.6f}")
    return lines

# === Проверка распределения ===
def report_species(structure, name):
    counter = Counter(site.species_string for site in reorder_by_type(structure))
    print(f"== {name} atom counts ==")
    for k in ['Sr', 'Ti', 'O']:
        print(f"{k}: {counter[k]}")

# === Генерация и запись ===
header = "\\SrTiO3: Pm-3m to Pnma transition"
block1 = structure_block(s1_super, 221)
block2 = structure_block(s2, 62)
footer = [
    "size 2 ! limit subgroup to cell doubling",
    "strain 0.6 1.6 ! minimum and maximum strain allowed",
    "neighbor 2.2 ! nearest-neighbor distance in structure at midpoint",
    "shuffle 1.5 ! maximum atomic displacement"
]

with open(output_file, "w") as f:
    f.write(header + "\n")
    f.write("\n".join(block1) + "\n")
    f.write("\n".join(block2) + "\n")
    f.write("\n".join(footer) + "\n")

# === Диагностика ===
report_species(s1_super, "Pm-3m (supercell)")
report_species(s2, "Pnma")

print(f"\n✅ comsubs.in successfully written with {len(block1)-3} + {len(block2)-3} atoms.")
