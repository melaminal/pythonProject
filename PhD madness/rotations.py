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

# Функция для создания суперячейки с учетом Glazer notation
def create_supercell_with_glazer(structure, glazer_notation):
    """
    Создает суперячейку 2x2x2 с вращениями октаэдров в соответствии с Glazer notation.

    Parameters:
    structure: Structure
        Исходная структура.
    glazer_notation: str
        Glazer notation, например, "a+a+c-" или "a0a0c-".

    Returns:
    Structure
        Структура с примененными вращениями и смещениями.
    """
    # Создаем суперячейку 2x2x2
    supercell = structure.copy()
    supercell.make_supercell([2, 2, 2])

    # Разбираем Glazer notation
    axes = ['x', 'y', 'z']
    directions = [glazer_notation[0], glazer_notation[2], glazer_notation[4]]  # a, b, c
    signs = [glazer_notation[1], glazer_notation[3], glazer_notation[5]]  # +, -, 0

    # Применяем вращения и смещения для каждой оси
    for axis, direction, sign in zip(axes, directions, signs):
        if sign == '0':
            continue  # Пропускаем ось без вращения
        apply_layered_rotation_with_displacement(supercell, axis, sign)

    return supercell


def apply_layered_rotation_with_displacement(structure, axis, sign):
    """
    Применяет вращение октаэдров и смещение атомов кислорода слоями вдоль заданной оси.

    Parameters:
    structure: Structure
        Структура, к которой применяется вращение.
    axis: str
        Ось вращения ('x', 'y', 'z').
    sign: str
        Направление вращения ('+' или '-').
    """
    angle_deg = 2  # Угол вращения в градусах
    angle_rad = np.radians(angle_deg)

    # Индекс оси (0 для x, 1 для y, 2 для z)
    axis_index = {'x': 0, 'y': 1, 'z': 2}[axis]

    # Находим координаты атомов Ti (центры вращения)
    titanium_sites = [site for site in structure if site.species_string == "Ti"]

    # Находим все атомы кислорода
    oxygen_sites = [site for site in structure if site.species_string == "O"]

    # Применяем вращение к каждому слою
    for ti_site in titanium_sites:
        ti_cart_coords = structure.lattice.get_cartesian_coords(ti_site.frac_coords)

        # Применяем вращение и смещение к атомам кислорода в той же плоскости
        for site in oxygen_sites:
            o_coords = site.frac_coords
            if not np.isclose(o_coords[axis_index], ti_site.frac_coords[axis_index]):
                continue  # Пропускаем атомы, которые не совпадают по координате оси

            # Чередуем направление вращения для разных слоев
            layer_index = np.round(ti_site.frac_coords[axis_index] * 2) % 2  # 0 или 1
            direction = 1 if sign == '+' else (-1 if layer_index == 1 else 1)
            adjusted_angle_rad = direction * angle_rad

            # Матрица вращения для текущего слоя
            rotation_matrix = {
                'x': np.array([
                    [1, 0, 0],
                    [0, np.cos(adjusted_angle_rad), -np.sin(adjusted_angle_rad)],
                    [0, np.sin(adjusted_angle_rad), np.cos(adjusted_angle_rad)]
                ]),
                'y': np.array([
                    [np.cos(adjusted_angle_rad), 0, np.sin(adjusted_angle_rad)],
                    [0, 1, 0],
                    [-np.sin(adjusted_angle_rad), 0, np.cos(adjusted_angle_rad)]
                ]),
                'z': np.array([
                    [np.cos(adjusted_angle_rad), -np.sin(adjusted_angle_rad), 0],
                    [np.sin(adjusted_angle_rad), np.cos(adjusted_angle_rad), 0],
                    [0, 0, 1]
                ])
            }[axis]

            # Вращаем атом кислорода
            o_cart_coords = structure.lattice.get_cartesian_coords(o_coords)
            relative_vector = o_cart_coords - ti_cart_coords
            rotated_vector = np.dot(rotation_matrix, relative_vector)
            new_cart_coords = ti_cart_coords + rotated_vector

            # Добавляем смещение по осям x и y в зависимости от слоя
            displacement = np.zeros(3)
            if axis == 'z':  # Смещение в плоскости xy
                if layer_index == 0:
                    displacement[0] = 0.01 * direction  # Смещение по x
                else:
                    displacement[1] = 0.01 * direction  # Смещение по y

            new_cart_coords += displacement
            site.frac_coords = np.mod(
                structure.lattice.get_fractional_coords(new_cart_coords), 1
            )


# Пример использования
glazer_notation = "a0a0c-"
supercell = create_supercell_with_glazer(EuTiO3_structure, glazer_notation)
output_file = "POSCAR_supercell_glazer.vasp"
with open(output_file, "w", encoding="utf-8") as f:
    poscar = Poscar(supercell)
    f.write(poscar.get_string())
print(f"Суперячейка с Glazer notation '{glazer_notation}' сохранена в файл {output_file}")
