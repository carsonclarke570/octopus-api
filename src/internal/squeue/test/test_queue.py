import pytest

from internal.squeue.squeue import SongQueue
from util.errors import APIException

class TestQueue:

    def setup_method(self):
        self.queue = SongQueue()
        self.queue.add("A", 1234)
        self.queue.add("B", 4321)
        self.queue.add("C", 1)
        self.queue.add("D", 2)

    def test_repr(self):
        assert self.queue.__repr__() == '[(A, 1), (B, 1), (C, 1), (D, 1)]'

    def test_peek(self):
        song = self.queue.peek()
        assert song.code == 'A'
        assert song.upvoted[0] == 1234

    def test_peek_fail(self):
        q = SongQueue()
        with pytest.raises(APIException):
            q.peek()

    def test_add(self):
        self.queue.add('E', 352532)
        assert len(self.queue.queue) == 5
        assert self.queue.queue[4].code == 'E'
        assert self.queue.queue[4].upvoted[0] == 352532

    def test_add_fail(self):
        with pytest.raises(APIException):
            self.queue.add('D', 2)

        with pytest.raises(APIException):
            self.queue.add('D', 352532)

    def test_remove(self):
        self.queue.remove('B')
        assert len(self.queue.queue) == 3
        assert self.queue.__repr__() == '[(A, 1), (C, 1), (D, 1)]'

    def test_remove_fail(self):
        with pytest.raises(APIException):
            self.queue.remove('b')
        
        assert len(self.queue.queue) == 4

    def test_upvote(self):
        self.queue.remove('B')
        self.queue.upvote('C', 3)
        assert self.queue.__repr__() == '[(C, 2), (A, 1), (D, 1)]'

        with pytest.raises(APIException):
            self.queue.upvote('C', 3)

        self.queue.upvote('C', 4)
        self.queue.upvote('C', 5)
        self.queue.upvote('C', 6)
        assert self.queue.__repr__() == '[(C, 5), (A, 1), (D, 1)]'

        self.queue.downvote('C', 4)
        assert self.queue.__repr__() == '[(C, 3), (A, 1), (D, 1)]'


    def test_downvote(self):
        self.queue.remove('B')
        self.queue.downvote('C', 1)
        assert self.queue.__repr__() == '[(A, 1), (D, 1), (C, -1)]'

        with pytest.raises(APIException):
            self.queue.downvote('C', 1)

        self.queue.downvote('C', 4)
        self.queue.downvote('C', 5)
        self.queue.downvote('C', 6)
        assert self.queue.__repr__() == '[(A, 1), (D, 1), (C, -4)]'