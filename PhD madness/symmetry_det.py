from pymatgen.io.vasp import Poscar
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
# poscar = Poscar.from_file("/home/dieguez/Desktop/EuTiO3/Rotations/a0a0a0/POSCAR")
poscar = Poscar.from_file("C:/Users/Maria/Desktop/POSCAR")
structure = poscar.structure

sga = SpacegroupAnalyzer(structure, symprec=0.0000001, angle_tolerance=1)

space_group = sga.get_space_group_symbol()
print(f"Space group: {space_group}")