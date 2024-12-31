from pymatgen.core import Lattice, Structure, PeriodicSite
import numpy as np
from pymatgen.io.vasp import Poscar

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

# Функция для вращения кислородных атомов вдоль заданной оси на определённый угол

def rotate_oxygen_atoms_supercell(structure, angle_deg, supercell_dim):
    """
    Вращает атомы кислорода в плоскости XY на заданный угол.
    Учитывает поворот в противоположную сторону для соседних ячеек.
    """
    angle_rad = np.radians(angle_deg)  # Преобразуем угол в радианы

    new_sites = []  # Список новых сайтов для структуры

    for site in structure.sites:
        if site.species_string == "O":
            frac_coords = site.frac_coords.copy()

            # Определяем четность или нечетность позиции ячейки
            cell_x = int(frac_coords[0] // 1)  # Индекс ячейки по X
            cell_y = int(frac_coords[1] // 1)  # Индекс ячейки по Y

            # Меняем направление вращения в шахматном порядке
            sign = 1 if (cell_x + cell_y) % 2 == 0 else -1

            # Оригинальная ячейка и соседние ячейки
            if abs(frac_coords[0] % 1) < 1e-6 and abs(frac_coords[1] % 1 - 0.5) < 1e-6:
                frac_coords[1] -= sign * np.sin(angle_rad)  # Смещение вдоль Y
            elif abs(frac_coords[0] % 1 - 0.5) < 1e-6 and abs(frac_coords[1] % 1) < 1e-6:
                frac_coords[0] += sign * np.sin(angle_rad)  # Смещение вдоль X

            new_sites.append(PeriodicSite(site.species, frac_coords, structure.lattice))
        else:
            new_sites.append(site)

    # Создаём новую структуру с обновлёнными сайтами
    modified_structure = Structure.from_sites(new_sites)

    # Создаём суперячейку на основе модифицированной структуры
    modified_structure.make_supercell(supercell_dim)

    return modified_structure

# Параметры вращения
angle_deg = 5  # Угол поворота в градусах
supercell_dim = [2, 2, 1]  # Размер суперячейки

# Вращаем структуру
rotated_structure = rotate_oxygen_atoms_supercell(EuTiO3_structure, angle_deg, supercell_dim)

# Печатаем повернутую структуру
print("Повернутая структура EuTiO3:")
print(rotated_structure)

# Экспортируем повернутую структуру в файл POSCAR с указанием кодировки
output_file = "POSCAR_EuTiO3_rotated_supercell"
with open(output_file, "w", encoding="utf-8") as f:
    poscar = Poscar(rotated_structure)
    f.write(poscar.get_string())
print(f"Повернутая структура сохранена в файл {output_file}")
