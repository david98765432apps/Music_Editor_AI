"""Utilities for building musical scales.

The module purposely implements only a small subset of music theory in a
concise and well documented form.  The goal is not to be exhaustive but
rather to provide dependable building blocks for algorithmic music
experiments.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List

_NOTE_SEQUENCE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

_FLAT_TO_SHARP = {
    "CB": "B",
    "DB": "C#",
    "EB": "D#",
    "FB": "E",
    "GB": "F#",
    "AB": "G#",
    "BB": "A#",
    "E#": "F",
    "B#": "C",
}

_MODE_INTERVALS: Dict[str, List[int]] = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 8, 10],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
}


def _normalize_note(note: str) -> str:
    """Convert user input into a canonical sharp-based representation."""

    if not note:
        raise ValueError("A note name is required")

    cleaned = note.strip().upper()
    if cleaned in _NOTE_SEQUENCE:
        return cleaned
    return _FLAT_TO_SHARP.get(cleaned, cleaned)


def _interval_notes(root_index: int, intervals: Iterable[int]) -> List[str]:
    return [
        _NOTE_SEQUENCE[(root_index + interval) % len(_NOTE_SEQUENCE)]
        for interval in intervals
    ]


def build_scale(root: str, mode: str = "major") -> List[str]:
    """Return the notes for the requested scale.

    Parameters
    ----------
    root:
        The tonic of the scale.  Flats (e.g. "Db") and sharps ("C#") are
        accepted.  All notes are normalised to sharps for simplicity.
    mode:
        Currently supported values are "major", "minor", "dorian" and
        "mixolydian".
    """

    normalised_mode = mode.lower()
    if normalised_mode not in _MODE_INTERVALS:
        raise KeyError(f"Unsupported mode: {mode}")

    normalised_root = _normalize_note(root)
    root_index = _NOTE_SEQUENCE.index(normalised_root)
    intervals = _MODE_INTERVALS[normalised_mode]
    return _interval_notes(root_index, intervals)


@dataclass(frozen=True)
class Scale:
    """Representation of a musical scale."""

    tonic: str
    mode: str
    notes: List[str]

    @classmethod
    def from_key_mode(cls, tonic: str, mode: str = "major") -> "Scale":
        return cls(
            tonic=_normalize_note(tonic),
            mode=mode.lower(),
            notes=build_scale(tonic, mode),
        )

    def degree(self, number: int) -> str:
        """Return the note at the given scale degree (1-indexed)."""

        if number <= 0:
            raise ValueError("Degree numbers start at 1")
        index = (number - 1) % len(self.notes)
        return self.notes[index]

    def rotated(self, steps: int) -> "Scale":
        """Return a copy of the scale rotated by the provided number of steps."""

        steps = steps % len(self.notes)
        return Scale(tonic=self.notes[steps], mode=self.mode, notes=self.notes[steps:] + self.notes[:steps])

    def to_dict(self) -> Dict[str, Iterable[str]]:
        """Serialise the scale into a JSON friendly dictionary."""

        return {"tonic": self.tonic, "mode": self.mode, "notes": list(self.notes)}


__all__ = ["Scale", "build_scale"]
