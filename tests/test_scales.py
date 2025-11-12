from music_editor_ai.scales import Scale, build_scale


def test_build_major_scale():
    assert build_scale("C", "major") == ["C", "D", "E", "F", "G", "A", "B"]


def test_build_minor_scale_with_flats():
    # Db minor should be normalised to sharps
    assert build_scale("Db", "minor") == ["C#", "D#", "E", "F#", "G#", "A", "B"]


def test_scale_degree_wraps_around():
    scale = Scale.from_key_mode("G", "major")
    assert scale.degree(8) == "G"
