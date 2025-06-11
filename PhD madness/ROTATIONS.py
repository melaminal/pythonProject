from pymatgen.core import Structure, PeriodicSite
from pymatgen.io.vasp import Poscar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

# Список возможных видов поворотов (Glazer notation)
Glazer_list = [
    "a0a0a0", "a0a0c+", "a0b+b+", "a+a+a+", "a+b+c+",
    "a0a0c-", "a0b-b-", "a-a-a-", "a0b-c-", "a-b-b-",
    "a-b-c-", "a0b+c-", "a+b-b-", "a+b-c-", "a+a+c-"
]

# Загружаем готовую 20-атомную структуру из POSCAR
structure_file = "POSCAR"  # Имя файла с исходной структурой
# Открываем файл с указанием кодировки
with open(structure_file, "r", encoding="utf-8") as f:
    file_content = f.read()

# Загружаем структуру из строки
EuTiO3_structure = Structure.from_str(file_content, fmt="poscar")

# Функция для обновления координат атомов в зависимости от Glazer notations
def update_atom_positions(structure, glazer_type):
    new_sites = []

    # Вращения для a0a0c+ P4/mbm
    if glazer_type == "a0a0c+":
        predefined_coords = {
            14: [0.25000+0.1, 0.25000+0.1, 0.75000],
            13: [0.25000+0.1, 0.25000+0.1, 0.25000],
            10: [0.75000+0.1, 0.25000-0.1, 0.75000],
            9: [0.75000+0.1, 0.25000-0.1, 0.25000],
            16: [0.75000-0.1, 0.75000-0.1, 0.75000],
            15: [0.75000-0.1, 0.75000-0.1, 0.25000],
            12: [0.25000-0.1, 0.75000+0.1, 0.75000],
            11: [0.25000-0.1, 0.75000+0.1, 0.25000]
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    # Вращения для a0a0c- I4/mcm
    elif glazer_type == "a0a0c-":
        predefined_coords = {
            14: [0.25000+0.1, 0.25000+0.1, 0.75000],
            13: [0.25000-0.1, 0.25000-0.1, 0.25000],
            10: [0.75000+0.1, 0.25000-0.1, 0.75000],
            9: [0.75000-0.1, 0.25000+0.1, 0.25000],
            16: [0.75000-0.1, 0.75000-0.1, 0.75000],
            15: [0.75000+0.1, 0.75000+0.1, 0.25000],
            12: [0.25000-0.1, 0.75000+0.1, 0.75000],
            11: [0.25000+0.1, 0.75000-0.1, 0.25000]
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    # Вращения для a0b-c- C2/m
    elif glazer_type == "a0b-c-":
        predefined_coords = {
            14: [0.25000+0.1, 0.25000+0.1, 0.75000],
            13: [0.25000-0.1, 0.25000-0.1, 0.25000],
            10: [0.75000+0.1, 0.25000-0.1, 0.75000-0.07],
            9: [0.75000-0.1, 0.25000+0.1, 0.25000+0.07],
            16: [0.75000-0.1, 0.75000-0.1, 0.75000],
            15: [0.75000+0.1, 0.75000+0.1, 0.25000],
            12: [0.25000-0.1, 0.75000+0.1, 0.75000+0.07],
            11: [0.25000+0.1, 0.75000-0.1, 0.25000-0.07],
            17: [0.00000 - 0.07, 0.50000 - 0.07, 0.00000],
            18: [0.00000 + 0.07, 0.50000 + 0.07, 0.50000],
            19: [0.50000 + 0.07, 0.00000 + 0.07, 0.00000],
            20: [0.50000 - 0.07, 0.00000 - 0.07, 0.50000]
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    # Вращения для a0b+c- Cmcm
    elif glazer_type == "a0b+c-":
        predefined_coords = {
            14: [0.25000 + 0.1, 0.25000 + 0.1, 0.75000],
            13: [0.25000 + 0.1, 0.25000 + 0.1, 0.25000],
            10: [0.75000 + 0.1, 0.25000 - 0.1, 0.75000-0.07],
            9: [0.75000 + 0.1, 0.25000 - 0.1, 0.25000+0.07],
            16: [0.75000 - 0.1, 0.75000 - 0.1, 0.75000],
            15: [0.75000 - 0.1, 0.75000 - 0.1, 0.25000],
            12: [0.25000 - 0.1, 0.75000 + 0.1, 0.75000+0.07],
            11: [0.25000 - 0.1, 0.75000 + 0.1, 0.25000-0.07],
            17: [0.00000 - 0.07, 0.50000 - 0.07, 0.00000],
            18: [0.00000 + 0.07, 0.50000 + 0.07, 0.50000],
            19: [0.50000 + 0.07, 0.00000 + 0.07, 0.00000],
            20: [0.50000 - 0.07, 0.00000 - 0.07, 0.50000]
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    # Вращения для a0b-b- Imma
    elif glazer_type == "a0b-b-":
        predefined_coords = {
            14: [0.25000+0.1, 0.25000+0.1, 0.75000],
            13: [0.25000-0.1, 0.25000-0.1, 0.25000],
            10: [0.75000+0.1, 0.25000-0.1, 0.75000-0.1],
            9: [0.75000-0.1, 0.25000+0.1, 0.25000+0.1],
            16: [0.75000-0.1, 0.75000-0.1, 0.75000],
            15: [0.75000+0.1, 0.75000+0.1, 0.25000],
            12: [0.25000-0.1, 0.75000+0.1, 0.75000+0.1],
            11: [0.25000+0.1, 0.75000-0.1, 0.25000-0.1],
            17: [0.00000 - 0.1, 0.50000 - 0.1, 0.00000],
            18: [0.00000 + 0.1, 0.50000 + 0.1, 0.50000],
            19: [0.50000 + 0.1, 0.00000 + 0.1, 0.00000],
            20: [0.50000 - 0.1, 0.00000 - 0.1, 0.50000]
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    # Вращения для a+b-b- Pnma
    elif glazer_type == "a+b-b-":
        predefined_coords = {
            14: [0.25000-0.1, 0.25000+0.6, 0.75000-0.05],
            13: [0.25000+0.1, 0.25000+1.1, 0.25000-0.05],
            10: [0.75000+0.1, 0.25000+0.9, 0.75000+0.05],
            9: [0.75000+0.1, 0.25000+0.9, 0.25000-0.05],
            16: [0.75000-0.1, 0.75000-0.1, 0.75000-0.05],
            15: [0.75000-0.1, 0.75000-0.1, 0.25000+0.05],
            12: [0.25000+0.1, 0.75000-0.4, 0.75000+0.05],
            11: [0.25000-0.1, 0.75000+0.1, 0.25000+0.05],
            17: [0.00000 - 0.1, 0.50000+0.15, 0.00000],
            18: [0.00000 + 0.1, 0.50000-0.15, 0.50000],
            19: [0.50000 - 0.1, 0.00000 - 0.15, 0.00000],
            20: [0.50000 + 0.1, 0.00000 + 0.15, 0.50000],
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    # Вращения для a-b-b- C2/c
    elif glazer_type == "a-b-b-":
        predefined_coords = {
            9: [0.68000, 0.32000, 0.35000],
            10: [0.82000, 0.18000, 0.65000],
            11: [0.32000, 0.68000, 0.15000],
            12: [0.18000, 0.82000, 0.85000],
            13: [0.18000, 0.18000, 0.15000],
            14: [0.32000, 0.32000, 0.85000],
            15: [0.82000, 0.82000, 0.35000],
            16: [0.68000, 0.68000, 0.65000],
            17: [-0.20000, 0.50000, 0.00000],
            18: [0.20000, 0.50000, 0.50000],
            19: [0.70000, 0.00000, 0.00000],
            20: [0.30000, 0.00000, 0.50000]
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    # Вращения для a-a-a- R-3c
    elif glazer_type == "a-a-a-":
        predefined_coords = {
            9: [0.65000, 0.35000, 0.35000],
            10: [0.85000, 0.15000, 0.65000],
            11: [0.35000, 0.65000, 0.15000],
            12: [0.15000, 0.85000, 0.85000],
            13: [0.15000, 0.15000, 0.15000],
            14: [0.35000, 0.35000, 0.85000],
            15: [0.85000, 0.85000, 0.35000],
            16: [0.65000, 0.65000, 0.65000],
            17: [-0.20000, 0.50000, 0.00000],
            18: [0.20000, 0.50000, 0.50000],
            19: [0.70000, 0.00000, 0.00000],
            20: [0.30000, 0.00000, 0.50000]
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    # Вращения для a-b-c- P-1
    elif glazer_type == "a-b-c-":
        predefined_coords = {
            9: [0.65000, 0.35000, 0.32000],
            10: [0.85000, 0.15000, 0.68000],
            11: [0.35000, 0.65000, 0.18000],
            12: [0.15000, 0.85000, 0.82000],
            13: [0.15000, 0.15000, 0.20000],
            14: [0.35000, 0.35000, 0.80000],
            15: [0.85000, 0.85000, 0.30000],
            16: [0.65000, 0.65000, 0.70000],
            17: [-0.10000, 0.46000, 0.00000],
            18: [0.10000, 0.54000, 0.50000],
            19: [0.60000, 0.04000, 0.00000],
            20: [0.40000, -0.04000, 0.50000]
        }
        for i, site in enumerate(structure.sites):
            if i + 1 in predefined_coords:
                new_coords = predefined_coords[i + 1]
                new_sites.append(PeriodicSite(site.species, new_coords, structure.lattice))
            else:
                new_sites.append(site)

    else:  # Если вращений нет
        new_sites = structure.sites

    return Structure.from_sites(new_sites)

# Пример обработки структуры с вращениями
glazer_type = "a0a0c-"  # Замените на нужный тип
updated_structure = update_atom_positions(EuTiO3_structure, glazer_type)

# Анализируем пространственную группу
analyzer = SpacegroupAnalyzer(updated_structure)
spacegroup = analyzer.get_space_group_symbol()  # Получить символ пространственной группы
spacegroup_number = analyzer.get_space_group_number()  # Получить номер пространственной группы

print(f"Пространственная группа: {spacegroup}, номер: {spacegroup_number}")

output_file = f"POSCAR_EuTiO3_{glazer_type}.vasp"
with open(output_file, "w", encoding="utf-8") as f:
    poscar = Poscar(updated_structure)
    f.write(poscar.get_string())
    print(f"Сохранена структура для {glazer_type} в файл {output_file}")
