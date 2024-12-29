from pymatgen.core import Lattice, Structure
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
    Вращает только те атомы кислорода, которые находятся в нужной плоскости
    вокруг указанной оси на заданный угол.
    """
    angle_rad = np.radians(angle_deg)  # Конвертируем угол в радианы
    rotation_matrix = {
        'x': np.array([[1, 0, 0], [0, np.cos(angle_rad), -np.sin(angle_rad)], [0, np.sin(angle_rad), np.cos(angle_rad)]]),
        'y': np.array([[np.cos(angle_rad), 0, np.sin(angle_rad)], [0, 1, 0], [-np.sin(angle_rad), 0, np.cos(angle_rad)]]),
        'z': np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0], [np.sin(angle_rad), np.cos(angle_rad), 0], [0, 0, 1]])
    }[axis]

    new_structure = structure.copy()  # Копируем структуру для модификаций

    # Находим координаты Ti
    ti_coords = None
    for site in new_structure:
        if site.species_string == "Ti":
            ti_coords = site.frac_coords
            break

    if ti_coords is None:
        raise ValueError("Атом Ti не найден в структуре.")

    # Вращаем только атомы кислорода в плоскости оси вращения
    for site in new_structure:
        if site.species_string == "O":
            o_coords = site.frac_coords

            # Для оси z: вращаем только атомы, где z(Ti) == z(O)
            if axis == 'z' and np.isclose(o_coords[2], ti_coords[2]):
                # Вращение в плоскости xy
                cart_coords = new_structure.lattice.get_cartesian_coords(o_coords)
                rotated_cart_coords = np.dot(rotation_matrix, cart_coords)
                site.frac_coords = new_structure.lattice.get_fractional_coords(rotated_cart_coords)

            # Для оси x: вращаем только атомы, где x(Ti) == x(O)
            elif axis == 'x' and np.isclose(o_coords[0], ti_coords[0]):
                # Вращение в плоскости yz
                cart_coords = new_structure.lattice.get_cartesian_coords(o_coords)
                rotated_cart_coords = np.dot(rotation_matrix, cart_coords)
                site.frac_coords = new_structure.lattice.get_fractional_coords(rotated_cart_coords)

            # Для оси y: вращаем только атомы, где y(Ti) == y(O)
            elif axis == 'y' and np.isclose(o_coords[1], ti_coords[1]):
                # Вращение в плоскости xz
                cart_coords = new_structure.lattice.get_cartesian_coords(o_coords)
                rotated_cart_coords = np.dot(rotation_matrix, cart_coords)
                site.frac_coords = new_structure.lattice.get_fractional_coords(rotated_cart_coords)

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

