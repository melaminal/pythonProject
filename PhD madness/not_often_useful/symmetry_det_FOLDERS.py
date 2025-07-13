import os
from pymatgen.io.vasp import Poscar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import pandas as pd

# symprec (симметрийная точность). Числовая погрешность (в Å) при сравнении атомных координат для определения симметрии.
# Чем меньше значение, тем жёстче критерий:
# 1e-3 — грубо (можно принять слегка искажённую структуру как высокосимметричную),
# 1e-5 — обычно разумно,
# 1e-7 — строго (хорошо для идеально релаксированных DFT-структур).

# angle_tolerance
# Угловая погрешность (в градусах) при определении симметрии: насколько отклонение углов от идеала (например, 90° или 120°)
# всё ещё считается допустимым. Чем меньше значение, тем жёстче критерий.
# angle_tolerance = 0.1 → только 90.0 ± 0.1° принимается как прямой угол;
# angle_tolerance = 1.0 → уже 89.0–91.0° допускается, можно «прощать» искажения.

# критерии симметрии выбраны по степени точности экспериментальных данных, обычно не превышающей 5 знаков после (.)
def analyze_symmetries(root_dir, symprec=1e-5, angle_tolerance=1):
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
analyze_symmetries("/home/mariia/EuTiO3/symmetry_det/BI/Pm-3m")
