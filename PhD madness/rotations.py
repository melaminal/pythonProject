from pymatgen.core import Lattice, Structure
from pymatgen.core import PeriodicSite
import numpy as np
from pymatgen.io.vasp import Poscar

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

# Функция для поворота кислородных атомов вокруг заданной оси
def rotate_oxygen_atoms(structure, axis, angle_deg):
    """
    Вращает атомы кислорода вокруг указанной оси на заданный угол,
    сохраняя согласованное вращение в одной плоскости.
    """
    angle_rad = np.radians(angle_deg)  # Угол в радианах

    # Матрицы вращения для всех осей
    rotation_matrices = {
        'x': np.array([
            [1, 0, 0],
            [0, np.cos(angle_rad), -np.sin(angle_rad)],
            [0, np.sin(angle_rad), np.cos(angle_rad)]
        ]),
        'y': np.array([
            [np.cos(angle_rad), 0, np.sin(angle_rad)],
            [0, 1, 0],
            [-np.sin(angle_rad), 0, np.cos(angle_rad)]
        ]),
        'z': np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0],
            [np.sin(angle_rad), np.cos(angle_rad), 0],
            [0, 0, 1]
        ])
    }

    rotation_matrix = rotation_matrices.get(axis)
    if rotation_matrix is None:
        raise ValueError("Некорректная ось вращения. Используйте 'x', 'y' или 'z'.")

    new_structure = structure.copy()

    # Находим атом Ti (центр вращения)
    ti_site = next((site for site in new_structure if site.species_string == "Ti"), None)
    if ti_site is None:
        raise ValueError("Атом Ti не найден в структуре.")

    ti_cart_coords = new_structure.lattice.get_cartesian_coords(ti_site.frac_coords)

    # Вращаем только атомы кислорода
    for site in new_structure:
        if site.species_string == "O":
            o_cart_coords = new_structure.lattice.get_cartesian_coords(site.frac_coords)

            # Пропускаем атомы, не находящиеся в плоскости вращения
            if axis == 'z' and not np.isclose(site.frac_coords[2], ti_site.frac_coords[2]):
                continue
            elif axis == 'x' and not np.isclose(site.frac_coords[0], ti_site.frac_coords[0]):
                continue
            elif axis == 'y' and not np.isclose(site.frac_coords[1], ti_site.frac_coords[1]):
                continue

            # Вращаем вектор относительно центра
            relative_vector = o_cart_coords - ti_cart_coords
            rotated_vector = np.dot(rotation_matrix, relative_vector)
            new_cart_coords = ti_cart_coords + rotated_vector

            # Обновляем положение атома
            site.frac_coords = np.mod(
                new_structure.lattice.get_fractional_coords(new_cart_coords), 1
            )

    return new_structure


# Параметры вращения
axis = 'z'  # Ось вращения
angle_deg = 5  # Угол поворота октаэдра

# Поворачиваем структуру
rotated_structure = rotate_oxygen_atoms(EuTiO3_structure, axis, angle_deg)

# Печатаем повернутую структуру
print("Повернутая структура EuTiO3:")
print(rotated_structure)

# Экспортируем повернутую структуру в файл POSCAR с указанием кодировки
output_file = "POSCAR_EuTiO3_rotated"
with open(output_file, "w", encoding="utf-8") as f:
    poscar = Poscar(rotated_structure)
    f.write(poscar.get_string())
print(f"Повернутая структура сохранена в файл {output_file}")

