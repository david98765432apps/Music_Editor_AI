"""Top-level package for the Music Editor AI utilities.

The package focuses on simple algorithms for generating scales,
chord progressions and lightweight melodic ideas that can be used as
starting points for songwriting experiments.  The functions are pure
Python and intentionally free from external dependencies so that they can
run in constrained environments.
"""

from .scales import Scale, build_scale
from .chords import generate_progression, triad_for_degree
from .melody import generate_melody
from .composer import create_song

__all__ = [
    "Scale",
    "build_scale",
    "triad_for_degree",
    "generate_progression",
    "generate_melody",
    "create_song",
]
