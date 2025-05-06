import os
from pymatgen.io.vasp import Poscar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import pandas as pd


def analyze_symmetries(root_dir, symprec=1e-7, angle_tolerance=1):
    results = []

    # Получаем список поддиректорий первого уровня
    for subdir in sorted(os.listdir(root_dir)):
        subdir_path = os.path.join(root_dir, subdir)
        contcar_path = os.path.join(subdir_path, "CONTCAR")

        if os.path.isdir(subdir_path) and os.path.isfile(contcar_path):
            try:
                poscar = Poscar.from_file(contcar_path)
                structure = poscar.structure
                sga = SpacegroupAnalyzer(structure, symprec=symprec, angle_tolerance=angle_tolerance)
                space_group = sga.get_space_group_symbol()
                results.append({"Subdirectory": subdir, "Space Group": space_group})
            except Exception as e:
                results.append({"Subdirectory": subdir, "Space Group": f"Error: {str(e)}"})

    # Формируем таблицу
    if results:
        df = pd.DataFrame(results)
        print(df.to_string(index=False))
    else:
        print("No CONTCAR files found in subdirectories.")


# Пример вызова
analyze_symmetries("/home/dieguez/Desktop/BI_ETO_after_P_calc/P4mm")
