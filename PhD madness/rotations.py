from pymatgen.core import Lattice, Structure
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

# Функция для определения атомов кислорода, которые должны быть сдвинуты

def get_target_oxygen_atoms(structure, axis):
    """
    Возвращает список атомов кислорода, которые находятся в той же плоскости,
    что и атом Ti, вдоль указанной оси.
    """
    target_atoms = []

    # Находим координаты Ti
    ti_coords = None
    for site in structure:
        if site.species_string == "Ti":
            ti_coords = site.frac_coords
            break

    if ti_coords is None:
        raise ValueError("Атом Ti не найден в структуре.")

    # Определяем, какие атомы кислорода находятся в той же плоскости
    for i, site in enumerate(structure):
        if site.species_string == "O":
            o_coords = site.frac_coords
            if axis == 'z' and np.isclose(o_coords[2], ti_coords[2]):
                target_atoms.append(i)

    return target_atoms

# Функция для вращения кислородных атомов вдоль заданной оси на определённый угол

def rotate_oxygen_atoms(structure, angle_deg):
    """
    Вращает атомы кислорода в плоскости XY на заданный угол.
    Для одного атома угол задаётся через смещение вдоль X, для другого — вдоль Y.
    Угол задаётся в градусах.
    """
    new_structure = structure.copy()  # Копируем структуру для модификаций
    target_atoms = get_target_oxygen_atoms(new_structure, 'z')  # Получаем целевые атомы

    angle_rad = np.radians(angle_deg)  # Преобразуем угол в радианы

    # Проверяем, что количество атомов кислорода в плоскости >= 2
    if len(target_atoms) < 2:
        raise ValueError("Недостаточно атомов кислорода для выполнения вращения.")

    # Первый атом (O1) смещается вдоль Y
    site1 = new_structure[target_atoms[0]]
    cart_coords1 = new_structure.lattice.get_cartesian_coords(site1.frac_coords)
    cart_coords1[1] -= np.sin(angle_rad)  # Смещение по Y
    site1.frac_coords = new_structure.lattice.get_fractional_coords(cart_coords1)

    # Второй атом (O2) смещается вдоль X
    site2 = new_structure[target_atoms[1]]
    cart_coords2 = new_structure.lattice.get_cartesian_coords(site2.frac_coords)
    cart_coords2[0] += np.sin(angle_rad)  # Смещение по X
    site2.frac_coords = new_structure.lattice.get_fractional_coords(cart_coords2)

    return new_structure

# Параметры вращения
angle_deg = 10  # Угол поворота в градусах

# Вращаем структуру
rotated_structure = rotate_oxygen_atoms(EuTiO3_structure, angle_deg)

# Печатаем повернутую структуру
print("Повернутая структура EuTiO3:")
print(rotated_structure)

# Экспортируем повернутую структуру в файл POSCAR с указанием кодировки
output_file = "POSCAR_EuTiO3_rotated"
with open(output_file, "w", encoding="utf-8") as f:
    poscar = Poscar(rotated_structure)
    f.write(poscar.get_string())
print(f"Повернутая структура сохранена в файл {output_file}")
