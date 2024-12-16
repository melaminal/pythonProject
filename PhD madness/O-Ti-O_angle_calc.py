import numpy as np

def read_poscar(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    lattice = np.array([list(map(float, lines[i].split())) for i in range(2, 5)])
    atoms = np.array([list(map(float, line.split())) for line in lines[8:]])
    return lattice, atoms

def calculate_angle(a, b, c):
    ab = a - b
    cb = c - b
    cos_theta = np.dot(ab, cb) / (np.linalg.norm(ab) * np.linalg.norm(cb))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    angle = np.degrees(np.arccos(cos_theta))
    return angle

def main():
    filename = "POSCAR_12.vasp"
    lattice, atoms = read_poscar(filename)

    print("Векторы решетки:")
    print(lattice)
    print("\nКоординаты атомов:")
    for atom in atoms:
        print(atom)

    new_atom = [0.25, 0.75, atoms[11][2]]
    atoms = np.vstack((atoms, new_atom))
    print("\nДобавлен атом:", new_atom)

    cart_coords = np.dot(atoms, lattice)

    atom_12_pos = cart_coords[11]  # Атом 12
    atom_21_pos = cart_coords[20]  # Атом 21

    angle = calculate_angle(atom_21_pos, cart_coords[5], atom_12_pos)
    print(f"Угол между атомами: {angle:.7f}°")

if __name__ == "__main__":
    main()