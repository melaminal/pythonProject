from pymatgen.core import Structure
from pymatgen.io.cif import CifWriter
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import glob, os

for poscar_path in glob.glob('C:/Users/Maria/Desktop/POSCAR'):
    s = Structure.from_file(poscar_path)

    # Определяем симметрию исходной структуры
    sga_orig = SpacegroupAnalyzer(s, symprec=1e-2, angle_tolerance=0.01)
    print("Исходная симметрия:", sga_orig.get_space_group_symbol())

    # Если нужно: получаем стандартную структуру
    # s_std = sga_orig.get_conventional_standard_structure()

    # Проверим симметрию стандартной структуры
    # sga_std = SpacegroupAnalyzer(s_std, symprec=1e-7, angle_tolerance=0.01)
    # print("Стандартная симметрия:", sga_std.get_space_group_symbol())

    # Пишем .cif без потерь симметрии
    cif_path = os.path.join(os.path.dirname(poscar_path), 'structure_std.cif')
    CifWriter(s, symprec=1e-7, angle_tolerance=0.01).write_file(cif_path)

print("Готово — CIF-ы лежат рядом с POSCAR")
