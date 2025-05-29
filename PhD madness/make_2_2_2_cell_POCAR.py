#!/usr/bin/env python
"""
Usage:
    python convert_EuTiO3.py [INPUT_POSCAR]

If no file is given, the script expects a file called POSCAR
in the working directory.
"""
import sys
import numpy as np
from pymatgen.core import Structure, Lattice

def main(fname="POSCAR"):

    # ---------- 1. исходная структура (20 атомов) ----------
    s0 = Structure.from_file(fname)

    # ---------- 2. строим новую ортогональную решётку ----------
    # старые базис-векторы
    v = s0.lattice.matrix.T            # 3×3, столбцы = v1, v2, v3
    a_len = np.linalg.norm(v[:, 0])    # |v1|  = a
    c_len = np.linalg.norm(v[:, 2])    # |v3|  = c  (= 2a в EuTiO3 Pm-3m)

    # новые векторы: (√2 a,0,0), (0,√2 a,0), (0,0,c)
    new_lat = Lattice([[np.sqrt(2)*a_len, 0, 0],
                       [0, np.sqrt(2)*a_len, 0],
                       [0, 0,              c_len]])

    # ---------- 3. пересчёт дробных координат ----------
    #   r_new = U⁻¹ · V · r_old
    U = new_lat.matrix.T
    V = v
    N = np.linalg.inv(U) @ V           # 3×3 линейное преобразование
    frac_new = (N @ s0.frac_coords.T).T % 1.0   # wrap внутри [0,1)

    s_unrot = Structure(
        new_lat,
        s0.species,
        frac_new,
        coords_are_cartesian=False
    )
    s_unrot.to(fmt="poscar", filename="POSCAR_unrot")  # 20 атомов

    # ---------- 4. строим 2 × 2 × 2 (8 кубиков) = 40 атомов ----------
    # для данной решётки достаточно удвоить только z (1,1,2);
    # поменяйте матрицу, если нужен иной множитель.
    s_super = s_unrot.copy()
    s_super.make_supercell([1, 1, 2])
    s_super.to(fmt="poscar", filename="POSCAR_2x2x2")  # 40 атомов

    print("✔ Готово: POSCAR_unrot (20 ат.) и POSCAR_2x2x2 (40 ат.)")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "POSCAR")
