import pytest

from internal.squeue.song import Song

class TestSong:

    def setup_method(self):
        self.song1 = Song("Code1", 1)
        self.song2 = Song("Code2", 2)
        self.song3 = Song("Code1", 2)

    def test_eq(self):
        assert self.song1 == self.song3

    def test_not_eq(self):
        assert self.song1 != self.song2
        assert self.song3 != self.song2

    def test_lt(self):
        self.song1.upvote(3)
        assert self.song1 > self.song2

    def test_not_lt(self):
        self.song1.upvote(3)
        assert (self.song1 < self.song2 == False)

    
