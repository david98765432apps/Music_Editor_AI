"""Helpers for producing lightweight melodic fragments."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import cycle
import random
from typing import Iterable, List, Optional, Sequence

from .scales import Scale

_DEFAULT_DURATIONS = (0.25, 0.5, 0.75, 1.0)


@dataclass(frozen=True)
class MelodyNote:
    """Representation of a single melodic event."""

    note: Optional[str]
    duration: float

    def to_dict(self) -> dict:
        return asdict(self)


def _duration_choices(pattern: Optional[Sequence[float]]) -> Iterable[float]:
    if pattern:
        for value in cycle(pattern):
            yield value
    else:
        while True:
            yield from _DEFAULT_DURATIONS


def generate_melody(
    scale: Scale,
    *,
    bars: int = 4,
    beats_per_bar: int = 4,
    rhythm_pattern: Optional[Sequence[float]] = None,
    allow_rests: bool = True,
    seed: Optional[int] = None,
) -> List[MelodyNote]:
    """Create a melody constrained to the provided scale."""

    if bars <= 0 or beats_per_bar <= 0:
        raise ValueError("Bars and beats must be positive integers")

    rng = random.Random(seed)
    total_beats = float(bars * beats_per_bar)
    beats_remaining = total_beats
    melody: List[MelodyNote] = []

    duration_iter = _duration_choices(rhythm_pattern)

    while beats_remaining > 1e-9:
        duration = next(duration_iter)
        duration = float(duration)
        if duration <= 0:
            raise ValueError("Durations must be positive numbers")
        if duration > beats_remaining:
            duration = beats_remaining

        note: Optional[str]
        if allow_rests and rng.random() < 0.2:
            note = None
        else:
            note = rng.choice(scale.notes)

        melody.append(MelodyNote(note=note, duration=round(duration, 3)))
        beats_remaining = round(beats_remaining - duration, 6)

    return melody


__all__ = ["MelodyNote", "generate_melody"]
