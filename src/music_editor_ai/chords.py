"""Simple helpers for building chord progressions."""

from __future__ import annotations

from typing import List, Sequence

from .scales import Scale


def triad_for_degree(scale: Scale, degree: int) -> List[str]:
    """Return the notes in the triad rooted at the provided scale degree."""

    if degree <= 0:
        raise ValueError("Degrees are one-indexed and must be positive")

    notes = scale.notes
    extended = notes + notes[:4]
    index = (degree - 1) % len(notes)
    return [extended[index], extended[index + 2], extended[index + 4]]


def generate_progression(scale: Scale, pattern: Sequence[int]) -> List[dict]:
    """Generate a chord progression for the supplied pattern of degrees."""

    progression = []
    for position, degree in enumerate(pattern, start=1):
        chord_notes = triad_for_degree(scale, degree)
        progression.append({"position": position, "degree": degree, "notes": chord_notes})
    return progression


__all__ = ["triad_for_degree", "generate_progression"]
