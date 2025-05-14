from pymatgen.core import Structure
from pymatgen.io.cif import CifWriter
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import glob, os

# === 1. пройдёмся по всем папкам ===
for poscar_path in glob.glob('C:/Users/Maria/Desktop/POSCAR'):
    # 2. читаем 20-атомную ячейку
    s = Structure.from_file(poscar_path)

    # 3. восстанавливаем симметрию (можно подправить symprec)
    sg = SpacegroupAnalyzer(s, symprec=1e-3, angle_tolerance=2)
    s_std = sg.get_conventional_standard_structure()

    # 4. пишем CIF
    cif_path = os.path.join(os.path.dirname(poscar_path), 'structure_std.cif')
    CifWriter(s_std, symprec=1e-3).write_file(cif_path)

print("Готово — CIF-ы лежат рядом с POSCAR")
