#!/usr/bin/env python3
"""
pol_from_vasp.py

Quick-and-dirty script that takes a VASP OUTCAR + matching CONTCAR
and prints the **physical** spontaneous-polarisation vector P
(in C m⁻² and µC cm⁻²).

How it works
------------
1.  Reads the lattice vectors from CONTCAR → volume Ω (Å³) and the three
    lattice-vector lengths |a|, |b|, |c| (Å).  The latter are the *quanta*
    that must be subtracted/added to bring the Berry-phase dipole onto the
    fundamental branch.
2.  Parses OUTCAR for the lines
       Ionic dipole moment: p[ion]=(
       Total electronic dipole moment: p[elc]=(
    adds them → total dipole **p_tot**  [e Å].
3.  For each Cartesian component α = x,y,z
       q_α = |a|, |b| or |c|                ← polarisation quantum [Å]
       p_phys_α = p_tot_α − round(p_tot_α / q_α) * q_α
4.  Converts **p_phys** to P via

       P =  e / Ω · p_phys   (remember: 1 e Å = e×10⁻¹⁰ C m)

   so:  P_α [C m⁻²] = (e * 10⁻¹⁰ / (Ω·10⁻³⁰)) · p_phys_α
                    = e * p_phys_α / Ω · 10²⁰
"""
import re
import sys
import numpy as np
from pathlib import Path

e = 1.602176634e-19          # C
A2M = 1e-10                  # 1 Å in m
VOL_A3_TO_M3 = 1e-30         # 1 Å³ in m³
C_TO_UC = 1e6                # C → µC
M2_TO_CM2 = 1e4              # m² → cm²

float_re = r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[EeDd][-+]?\d+)?'

dipole_line = re.compile(
    r'p\[(?P<tag>\w+)]\s*='          # p[ion], p[sp1] … p[elc] =
    r'\(\s*'                         # opening parenthesis
    r'(?P<x>' + float_re + r')\s+'   # x
    r'(?P<y>' + float_re + r')\s+'   # y
    r'(?P<z>' + float_re + r')\s*'   # z
    r'\)',                           # closing parenthesis
    re.I
)

def read_concar(concar_path):
    with open(concar_path) as f:
        lines = f.readlines()

    scale = float(lines[1].split()[0])

    # векторы a, b, c  (Å)
    a = np.fromstring(lines[2], sep=" ") * scale
    b = np.fromstring(lines[3], sep=" ") * scale
    c = np.fromstring(lines[4], sep=" ") * scale

    volume = abs(np.dot(a, np.cross(b, c)))      # Å³
    return volume, a, b, c

def parse_outcar(path="OUTCAR"):
    dip_vecs = {}
    with open(path, 'r') as f:
        for line in f:
            m = dipole_line.search(line)
            if m:
                tag = m.group('tag')          # ion, sp1, sp2, elc
                vec = np.array([
                    float(m.group('x').replace('D', 'E')),
                    float(m.group('y').replace('D', 'E')),
                    float(m.group('z').replace('D', 'E'))
                ])
                dip_vecs[tag] = vec

    # обязательно найдём p[ion] и p[elc]
    try:
        return dip_vecs['ion'] + dip_vecs['elc']
    except KeyError:
        raise RuntimeError("Не найдены строки p[ion]=(...) или p[elc]=(...) в OUTCAR")

def reduce_to_branch(p_tot, lattice_vectors):
    """
    lattice_vectors : (3, 3) ndarray, rows = a, b, c in Å
    p_tot           : (3,)   ndarray, dipole in e·Å
    """
    L = lattice_vectors.T          # 3×3 (столбцы — векторы)
    frac = np.linalg.solve(L, p_tot)        # p_tot = L·frac  ⇒  frac = L⁻¹ p_tot
    frac -= np.round(frac)         # переводим в диапазон (-0.5, 0.5]
    return L @ frac                # физический диполь e·Å

def minimize_norm(p0, lattice_vectors):
    """
    Сводим дипольный вектор p0 к ближайшей ветви (минимизируем |p|),
    разрешая сдвиги на целые и полу-кванты ±1, ±½ вдоль a, b, c.

    Parameters
    ----------
    p0               : ndarray, shape (3,)
                       исходный дипольный момент [e Å]
    lattice_vectors  : ndarray, shape (3, 3)
                       a, b, c строками (Å)

    Returns
    -------
    ndarray, shape (3,)
        p_phys — диполь на физической ветви [e Å]
    """
    L = lattice_vectors       # (3,3) rows = a, b, c
    # полный перебор коэффициентов (na, nb, nc)
    best = p0
    best_norm2 = np.dot(p0, p0)

    for na in (-1, -0.5, 0, 0.5, 1):
        for nb in (-1, -0.5, 0, 0.5, 1):
            for nc in (-1, -0.5, 0, 0.5, 1):
                cand = p0 + na*L[0] + nb*L[1] + nc*L[2]
                n2 = np.dot(cand, cand)
                if n2 < best_norm2 - 1e-10:   # маленький запас, чтобы избегать шумовых срабатываний
                    best, best_norm2 = cand, n2

    return best


def main(outcar="/home/dieguez/Desktop/BI_ETO_after_P_calc/a0a0c-_or_I4_mcm/102_5_percent/OUTCAR", concar="/home/dieguez/Desktop/BI_ETO_after_P_calc/a0a0c-_or_I4_mcm/102_5_percent/CONTCAR"):
    Ω_A3, a_vec, b_vec, c_vec = read_concar(concar)
    p_tot = parse_outcar(outcar)
    p_phys = reduce_to_branch(p_tot, np.vstack([a_vec, b_vec, c_vec]))
    p_phys = minimize_norm(p_phys, np.vstack([a_vec, b_vec, c_vec]))

    # Polarisation (C m⁻²)
    P = e * p_phys / Ω_A3 * 1e20
    P_uc_cm2 = P * C_TO_UC / M2_TO_CM2

    print("Volume Ω  = %.6f  Å³" % Ω_A3)
    print("Dipole, total  p_tot [e Å]  =", p_tot)
    print("Dipole, branch p_phys[e Å]  =", p_phys)
    print("\nPolarisation P   [C  m⁻²]  = (%.4e, %.4e, %.4e)" % tuple(P))
    print("              P [µC cm⁻²]  = (%.4f,  %.4f,  %.4f)" % tuple(P_uc_cm2))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        # if only one file supplied, treat it as OUTCAR and use default CONTCAR
        main(sys.argv[1], "CONTCAR")
    else:
        main()
