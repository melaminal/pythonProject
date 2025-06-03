from pymatgen.io.cif import CifParser
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

structure = CifParser("C:/Users/Maria/Desktop/structure_Pnma_exact.cif").get_structures()[0]
sga = SpacegroupAnalyzer(structure, symprec=1e-8)
print("Space group:", sga.get_space_group_symbol())
