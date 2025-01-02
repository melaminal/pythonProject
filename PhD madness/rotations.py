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

# Функция для вращения атомов кислорода в базовой ячейке

def rotate_atoms_in_unit_cell(structure, angle_deg):
    """
    Вращает атомы кислорода в базовой ячейке.
    """
    angle_rad = np.radians(angle_deg)  # Преобразуем угол в радианы
    new_sites = []  # Список новых сайтов для структуры

    for site in structure.sites:
        frac_coords = site.frac_coords.copy()
        if site.species_string == "O":
            # Применяем вращение для атомов кислорода
            if np.isclose(frac_coords[0], 0.0, atol=1e-6) and np.isclose(frac_coords[1], 0.5, atol=1e-6):
                frac_coords[1] -= np.sin(angle_rad)
            elif np.isclose(frac_coords[0], 0.5, atol=1e-6) and np.isclose(frac_coords[1], 0.0, atol=1e-6):
                frac_coords[0] += np.sin(angle_rad)

            # Печатаем координаты после вращения для проверки
            print(f"Вращение в базовой ячейке, после вращения: {frac_coords}")

        # Обновляем сайт
        new_sites.append(PeriodicSite(site.species, frac_coords, structure.lattice))

    # Создаём новую структуру с обновлёнными сайтами
    return Structure.from_sites(new_sites)

# Параметры вращения
angle_deg = 10  # Угол поворота в градусах
supercell_dim = [2, 2, 1]  # Размер суперячейки

# Вращаем базовую ячейку
rotated_unit_cell = rotate_atoms_in_unit_cell(EuTiO3_structure, angle_deg)

# Создаём суперячейку из повернутой базовой ячейки
rotated_unit_cell.make_supercell(supercell_dim)

# Печатаем повернутую суперячейку
print("Повернутая суперячейка EuTiO3:")
print(rotated_unit_cell)

# Экспортируем структуру в файл POSCAR с указанием кодировки
output_file = "POSCAR_EuTiO3_supercell_rotated"
with open(output_file, "w", encoding="utf-8") as f:
    poscar = Poscar(rotated_unit_cell)
    f.write(poscar.get_string())
print(f"Суперячейка сохранена в файл {output_file}")
