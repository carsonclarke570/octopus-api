import json

from util.errors import APIException
from util.serial.serialize import Serializable
from internal.squeue.song import Song

class SongQueue(Serializable):

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return str(self.queue)

    def peek(self):
        """ Finds the queue element with the highest priority
        
        :return: Song with the highest priority
        """
        if len(self.queue) < 1:
            raise APIException('Queue has no songs')

        return self.queue[0]

    def pop(self):
        """ Removes the song with the highest priority
        
        :return: the spotify song code of the removed song
        """
        return self.queue.pop(0)

    def add(self, code, cid):
        """ Adds a new song to the queue
        
        :param code: spotify code of song to add
        :param cid: id of user who added this song
        :return:
        """
        new_song = Song(code, cid)
        if new_song in self.queue:
            raise APIException("Song already exists in queue")
        
        self.queue.append(new_song)
        self.update()

    def remove(self, code):
        """ Removes a song from the queue
        
        :param code: spotify code of song to remove
        :return:
        """
        try:
            idx = self.queue.index(Song(code, 0))
        except ValueError as e:
            raise APIException(str(e))
        
        del self.queue[idx]
                
    def upvote(self, code, cid):
        """ Upvotes the song in the queue with the matching spotify code
        AssertionError if the id has already upvoted
        
        :param code: spotify code of song to upvote
        :param cid: id of user who upvoted this song
        :return:
        """
        idx = self.queue.index(Song(code, 0))
        song = self.queue[idx]
        if cid in song.upvoted:
            raise APIException("User has already upvoted")  # No duplicate upvotes

        if cid in song.downvoted:                          # User cannot upvote and downvote
            song.remove_downvoted(cid)

        song.upvote(cid)
        self.update()

    def downvote(self, code, cid):
        """ Downvotes the song in the queue with the matchin spotify code
        AssertionError if the id has already downvoted

        :param code: spotify code of song to downvote
        :param cid: id of user who downvoted this song
        :return:
        """
        idx = self.queue.index(Song(code, 0))
        song = self.queue[idx]
        if cid in song.downvoted:
            raise APIException("User has already downvoted")  # No duplicate upvotes

        if cid in song.upvoted:             # User cannot upvote and downvote
            song.remove_upvoted(cid)

        song.downvote(cid)
        self.update()

    def update(self):
        """ Updates the queue when a song is added

        :return:
        """
        self.queue.sort(reverse=True)

    def encode(self):
        songs = []
        for s in self.queue:
            songs.append(s.encode())

        return json.dumps(songs)

    @classmethod
    def decode(cls, data):
        data = json.loads(data)
        q = cls()
        for x in data:
            q.queue.append(Song.decode(x))
            
        return q
