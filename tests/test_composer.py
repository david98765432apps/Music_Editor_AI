import pytest

from music_editor_ai import create_song


def test_create_song_structure():
    song = create_song(bars=2, beats_per_bar=4, allow_rests=False, seed=42)

    assert song["scale"]["tonic"] == "C"
    assert len(song["progression"]) == 4

    melody = song["melody"]
    total_duration = sum(note["duration"] for note in melody)
    assert total_duration == pytest.approx(8.0)
    assert all(note["note"] is None or note["note"] in song["scale"]["notes"] for note in melody)
