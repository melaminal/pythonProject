from pymatgen.core import Lattice, Structure, PeriodicSite
import numpy as np
from pymatgen.io.vasp import Poscar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

# Список возможных видов поворотов (Glazer notation)
Glazer_list = [
    "a0a0a0", "a0a0c+", "a0b+b+", "a+a+a+", "a+b+c+",
    "a0a0c-", "a0b-b-", "a-a-a-", "a0b-c-", "a-b-b-",
    "a-b-c-", "a0b+c-", "a+b-b-", "a+b-c-", "a+a+c-"
]
correct_space_group_numbers = [
    221, 127, 139, 204, 71,
    140, 74, 167, 12, 15,
    2, 63, 62, 11, 137
]

# Определяем параметры решётки (в ангстремах)
a = 3.905
lattice = Lattice.from_parameters(a, a, a, 90, 90, 90)  # Кубическая решётка

# Определяем атомы и их позиции
species = ["Eu", "Ti", "O", "O", "O"]  # Элементы
coords = [
    [0.0, 0.0, 0.0],  # Eu
    [0.5, 0.5, 0.5],  # Ti
    [0.0, 0.5, 0.5],  # O1
    [0.5, 0.0, 0.5],  # O2
    [0.5, 0.5, 0.0],  # O3
]  # Долевые координаты (в единицах решётки)

# Создаём структуру
EuTiO3_structure = Structure(lattice, species, coords)

# Функция для создания суперячейки 2x2x2
def create_supercell(structure, dimensions):
    structure.make_supercell(dimensions)
    return structure

# Функция для определения четности ячейки атома титана
def is_even_cell(ti_site):
    """
    Определяет четность ячейки атома титана.
    Четная, если ratio == 1, нечётная, если ratio кратно 3 (все остальные четные).
    """
    x, y = ti_site.frac_coords[0], ti_site.frac_coords[1]
    larger, smaller = max(x, y), min(x, y)
    ratio = larger / smaller if smaller > 0 else float('inf')
    is_odd = int(round(ratio)) % 3 == 0
    is_even = not is_odd
    print(f"Ti atom at {ti_site.frac_coords}: {'even' if is_even else 'odd'} (ratio = {ratio:.6f})")
    return is_even

# Функция для привязки кислородных атомов к титану
def map_oxygen_to_titanium(structure):
    """
    Привязывает два кислородных атома к каждому атому титана.
    Возвращает словарь, где ключ - индекс Ti, значение - индексы O.
    """
    ti_to_o_map = {}
    for i, ti_site in enumerate(structure.sites):
        if ti_site.species_string == "Ti":
            ti_to_o_map[i] = []
            for j, o_site in enumerate(structure.sites):
                if o_site.species_string == "O":
                    # Проверяем условия для двух связанных атомов кислорода
                    if (
                        np.isclose(o_site.frac_coords[0], ti_site.frac_coords[0], atol=1e-6) and
                        np.isclose(o_site.frac_coords[1], ti_site.frac_coords[1] - 0.25, atol=1e-6) and
                        np.isclose(o_site.frac_coords[2], ti_site.frac_coords[2], atol=1e-6)
                    ):
                        ti_to_o_map[i].append(j)
                    elif (
                        np.isclose(o_site.frac_coords[0], ti_site.frac_coords[0] - 0.25, atol=1e-6) and
                        np.isclose(o_site.frac_coords[1], ti_site.frac_coords[1], atol=1e-6) and
                        np.isclose(o_site.frac_coords[2], ti_site.frac_coords[2], atol=1e-6)
                    ):
                        ti_to_o_map[i].append(j)
                    if len(ti_to_o_map[i]) == 2:  # Привязываем только 2 кислорода
                        break
            print(f"Ti atom index {i} at {ti_site.frac_coords} is linked to O atom indices: {ti_to_o_map[i]}")
            for o_index in ti_to_o_map[i]:
                print(f"    Linked O atom at {structure[o_index].frac_coords}")
    return ti_to_o_map

# Функция для вращения кислородных атомов

def rotate_oxygen_atoms_in_supercell(structure, angle_deg, ti_to_o_map, glazer_type):
    """
    Применяет вращение кислородных атомов на основе четности ячейки титана и слоя z.
    Если знак в Glazer notations для оси "+", оба слоя вращаются одинаково.
    Если знак "-", во втором слое четные ячейки вращаются как нечетные в первом слое, и наоборот.
    """
    if glazer_type == "a0a0a0":
        # Если все оси имеют поворот 0, ничего не делаем
        print("No rotation applied for Glazer notation: a0a0a0")
        return structure

    angle_rad = np.radians(angle_deg)
    new_sites = []

    # Проверяем знак оси "c" из Glazer notations
    c_sign = glazer_type[-1] if glazer_type[-2] == 'c' else '+'

    for i, site in enumerate(structure.sites):
        frac_coords = site.frac_coords.copy()
        if i in [idx for sublist in ti_to_o_map.values() for idx in sublist]:
            # Найти родительский атом Ti
            parent_ti = next(ti for ti, oxygens in ti_to_o_map.items() if i in oxygens)

            # Определить четность ячейки атома титана
            is_even = is_even_cell(structure[parent_ti])

            # Определить слой (нижний или верхний) по z
            is_upper_layer = np.isclose(frac_coords[2], 0.75)

            # Меняем направление вращения в верхнем слое только если знак "-"
            if is_upper_layer and c_sign == '-':
                is_even = not is_even

            # Направление вращения
            sign = 1 if is_even else -1

            # Поворачиваем атом кислорода
            if i == ti_to_o_map[parent_ti][0]:
                frac_coords[1] -= sign * np.sin(angle_rad)  # Уменьшить или увеличить y-координату
            elif i == ti_to_o_map[parent_ti][1]:
                frac_coords[0] += sign * np.sin(angle_rad)  # Увеличить или уменьшить x-координату

        new_sites.append(PeriodicSite(site.species, frac_coords, structure.lattice))

    return Structure.from_sites(new_sites)

# Параметры вращения
angle_deg = 5
supercell_dim = [2, 2, 2]  # Два слоя по z

# Создаём суперячейку
EuTiO3_structure.make_supercell(supercell_dim)

# Создаём карту Ti-O
ti_to_o_map = map_oxygen_to_titanium(EuTiO3_structure)

# Поворачиваем кислородные атомы в соответствии с Glazer notations
glazer_type = "a0a0a0"
rotated_structure = rotate_oxygen_atoms_in_supercell(EuTiO3_structure, angle_deg, ti_to_o_map, glazer_type)

# Печатаем повернутую суперячейку
print("Повернутая суперячейка EuTiO3:")
print(rotated_structure)

# Анализ симметрии
symmetry_finder = SpacegroupAnalyzer(rotated_structure, symprec=1e-3)

# Экспорт компактной структуры в POSCAR
output_file_compact = "POSCAR_EuTiO3_supercell_compact"
with open(output_file_compact, "w", encoding="utf-8") as f:
    poscar_compact = Poscar(rotated_structure)
    f.write(poscar_compact.get_string())
print(f"Компактная суперячейка сохранена в файл {output_file_compact}")