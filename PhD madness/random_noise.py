import random

def modify_coordinates(file_path, output_path, start_line=9, end_line=48, delta_range=(-0.02, 0.02)):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(start_line - 1, end_line):  # Индексация с 0, поэтому start_line-1
        parts = lines[i].split()
        if len(parts) >= 3:  # Проверяем, есть ли хотя бы три столбца (x, y, z)
            new_coords = [
                str(float(parts[j]) + random.uniform(*delta_range)) for j in range(3)
            ]
            lines[i] = " ".join(new_coords) + "\n"

    with open(output_path, 'w') as file:
        file.writelines(lines)

    print(f"Файл {output_path} сохранён с изменёнными координатами.")

# Пример использования
input_file = "POSCAR_40atoms"  # Заменить на реальный путь
output_file = "POSCAR_40_atoms_with_noise"  # Заменить на реальный путь
modify_coordinates(input_file, output_file)
