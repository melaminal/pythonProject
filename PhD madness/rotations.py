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
    Вращает атомы кислорода вокруг заданной оси на заданный угол.
    Все атомы вращаются в одну сторону относительно центра (атома Ti).
    """
    angle_rad = np.radians(angle_deg)  # Угол в радианах

    # Определяем матрицу вращения для заданной оси
    rotation_matrix = {
        'x': np.array([[1, 0, 0], [0, np.cos(angle_rad), -np.sin(angle_rad)], [0, np.sin(angle_rad), np.cos(angle_rad)]]),
        'y': np.array([[np.cos(angle_rad), 0, np.sin(angle_rad)], [0, 1, 0], [-np.sin(angle_rad), 0, np.cos(angle_rad)]]),
        'z': np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0], [np.sin(angle_rad), np.cos(angle_rad), 0], [0, 0, 1]])
    }[axis]

    new_structure = structure.copy()  # Копируем структуру

    # Находим центр вращения (атом Ti)
    ti_coords = None
    for site in new_structure:
        if site.species_string == "Ti":
            ti_coords = site.frac_coords
            ti_cart_coords = new_structure.lattice.get_cartesian_coords(ti_coords)
            break

    if ti_coords is None:
        raise ValueError("Атом Ti не найден в структуре.")

    # Вращаем только атомы кислорода
    for site in new_structure:
        if site.species_string == "O":
            o_coords = site.frac_coords
            o_cart_coords = new_structure.lattice.get_cartesian_coords(o_coords)

            # Вектор от Ti к кислороду
            relative_vector = o_cart_coords - ti_cart_coords

            # Поворачиваем вектор в одну сторону
            rotated_vector = np.dot(rotation_matrix, relative_vector)

            # Новые декартовые координаты кислорода
            new_cart_coords = ti_cart_coords + rotated_vector

            # Конвертируем обратно в дробные координаты
            new_frac_coords = new_structure.lattice.get_fractional_coords(new_cart_coords)

            # Обновляем координаты атома
            site.frac_coords = new_frac_coords

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

