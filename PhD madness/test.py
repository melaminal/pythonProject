from crystal_toolkit.renderables import StructureMoleculeComponent
from crystal_toolkit.helpers.utils import show_structure
from pymatgen.core import Lattice, Structure

# Тестовая структура
a = 3.905
lattice = Lattice.from_parameters(a, a, a, 90, 90, 90)
species = ["Eu", "Ti", "O", "O", "O"]
coords = [
    [0.5, 0.5, 0.5],  # Eu
    [0.0, 0.0, 0.0],  # Ti
    [0.0, 0.5, 0.5],  # O1
    [0.5, 0.0, 0.5],  # O2
    [0.5, 0.5, 0.0],  # O3
]
structure = Structure(lattice, species, coords)

# Визуализация
try:
    show_structure(structure)
except Exception as e:
    print(f"Ошибка при использовании crystal_toolkit: {e}")
