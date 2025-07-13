import os
from pymatgen.io.vasp import Poscar
from pymatgen.io.cif import CifParser
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

# Ввод имени файла
# filename = "C:/Users/Maria/Desktop/structure_Pnma_exact.cif"
filename = "C:/Users/Maria/Desktop/POSCAR"
# filename = "/home/dieguez/Desktop/POSCAR"

# Определение расширения
ext = os.path.splitext(filename)[1].lower()

# Считывание структуры в зависимости от формата
if ext == ".cif":
    parser = CifParser(filename)
    structure = parser.get_structures(z)[0]
elif ext in [".vasp", ".poscar", ""]:  # иногда POSCAR без расширения
    poscar = Poscar.from_file(filename)
    structure = poscar.structure
else:
    raise ValueError(f"Неподдерживаемый формат файла: {ext}")

# Анализ симметрии
sga = SpacegroupAnalyzer(structure, symprec=1e-4, angle_tolerance=1)
structure_std = sga.get_conventional_standard_structure(international_monoclinic=True)

# Повторный анализ — без перехода к примитивной ячейке
sga_std = SpacegroupAnalyzer(structure, symprec=1e-4, angle_tolerance=1)
print("Standard space group:", sga_std.get_space_group_symbol())

