# Music_Editor_AI

A lightweight toolkit for generating musical ideas from the command line.
The project focuses on simple scale calculations, chord progressions and
melodic sketches so that you can explore song ideas quickly without heavy
dependencies.

## Installation

Create a virtual environment and install the project in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

The package does not have any third-party dependencies, so installation is
instant.

## Command line usage

Generate a short sketch using the built-in CLI:

```bash
python -m music_editor_ai.cli --key D --mode dorian --bars 4 --progression 1 4 1 5 --seed 123
```

The command prints a JSON structure containing the scale, chord progression
and melody.  Provide `--output song.json` to store the result in a file.
Disable melodic rests with `--no-rests`.

## Python API

```python
from music_editor_ai import create_song

song = create_song(key="A", mode="minor", bars=8, beats_per_bar=3, seed=99)
print(song["progression"])
```

## Running tests

```bash
pytest
```
