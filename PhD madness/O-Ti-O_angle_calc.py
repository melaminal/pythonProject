import numpy as np

def read_poscar(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    lattice = np.array([list(map(float, lines[i].split())) for i in range(2, 5)])
    atom_counts = list(map(int, lines[6].split()))
    total_atoms = sum(atom_counts)

    atoms = []
    for line in lines[8:8 + total_atoms]:
        coords = list(map(float, line.strip().split()[:3]))
        atoms.append(coords)

    atoms = np.array(atoms)
    return lattice, atoms

def calculate_angle(a, b, c):
    ab = a - b
    cb = c - b
    cos_theta = np.dot(ab, cb) / (np.linalg.norm(ab) * np.linalg.norm(cb))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    angle = np.degrees(np.arccos(cos_theta))
    return angle

def main():
    filename = "/home/dieguez/Desktop/POSCAR"
    lattice, atoms = read_poscar(filename)

    print("Векторы решетки:")
    print(lattice)

    print("\nКоординаты атомов (Direct):")
    for i, atom in enumerate(atoms, 1):
        print(f"{i:2d}: {atom}")

    # Добавление нового атома с таким же z, как у атома 12
    z_coord = atoms[11][2]  # атом 12 — индекс 11
    new_atom = [0.25, 0.75, z_coord]
    atoms = np.vstack((atoms, new_atom))
    print(f"\nДобавлен атом (номер 21): {new_atom}")

    # Переводим в декартовы координаты
    cart_coords = np.dot(atoms, lattice)

    # Индексы: 12 (11), 6 (5), новый (20)
    pos_12 = cart_coords[11]
    pos_6 = cart_coords[5]
    pos_new = cart_coords[-1]  # индекс 20

    angle = calculate_angle(pos_12, pos_6, pos_new)
    print(f"\nУгол между атомами 12–6–21: {angle:.7f}°")

if __name__ == "__main__":
    main()
