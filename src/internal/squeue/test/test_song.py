import pytest

from internal.squeue.song import Song

def test_eq():
    one = Song("Code1", 1)
    two = Song("Code1", 2)
    assert one == two

    three = Song("Code2", 2)
    assert one != three
    assert two != three
