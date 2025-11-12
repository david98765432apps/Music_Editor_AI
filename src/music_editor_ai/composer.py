"""High level helpers that combine the building blocks into a song."""

from __future__ import annotations

from typing import Optional, Sequence

from .chords import generate_progression
from .melody import generate_melody
from .scales import Scale

_DEFAULT_PROGRESSION = (1, 5, 6, 4)


def create_song(
    *,
    key: str = "C",
    mode: str = "major",
    bars: int = 4,
    beats_per_bar: int = 4,
    progression: Optional[Sequence[int]] = None,
    allow_rests: bool = True,
    seed: Optional[int] = None,
) -> dict:
    """Create a simple song blueprint."""

    musical_scale = Scale.from_key_mode(key, mode)
    degrees = progression if progression is not None else _DEFAULT_PROGRESSION
    chords = generate_progression(musical_scale, degrees)
    melody = generate_melody(
        musical_scale,
        bars=bars,
        beats_per_bar=beats_per_bar,
        allow_rests=allow_rests,
        seed=seed,
    )

    return {
        "scale": musical_scale.to_dict(),
        "progression": chords,
        "melody": [note.to_dict() for note in melody],
    }


__all__ = ["create_song"]
