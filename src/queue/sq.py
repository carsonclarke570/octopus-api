from song import Song


class SongQueue:
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return str(self.queue)

    def peek(self):
        """
        Finds the queue element with the highest priority
        :return: Song with the highest priority
        """
        return self.queue[0]

    def pop(self):
        """
        Removes the song with the highest priority
        :return: the spotify song code of the removed song
        """
        tmp = self.peek()
        self.queue.pop(0)
        return tmp

    def add(self, code, ip):
        """
        Adds a new song to the queue
        :param code: spotify code of song to add
        :param ip: ip of user who added this song
        :return:
        """
        new_song = Song(code, 1, ip)
        assert (new_song not in self.queue), "No duplicates allowed in queue"
        self.queue.append(new_song)
        self.update()

    def remove(self, code):
        """
        Removes a song from the queue
        :param code: spotify code of song to remove
        :return:
        """
        pass

    def upvote(self, code, ip):
        """
        Upvotes the song in the queue with the matching spotify code
        AssertionError if the ip has already upvoted
        :param code: spotify code of song to upvote
        :param ip: ip of user who upvoted this song
        :return:
        """
        idx = self.queue.index(Song(code, 0, 0))
        song = self.queue[idx]
        assert (ip not in song.get_upvoted())      # No duplicate upvotes
        if ip in song.get_downvoted():             # User cannot upvote and downvote
            song.remove_downvoted(ip)
        song.upvote(ip)
        self.update()

    def downvote(self, code, ip):
        """
        Downvotes the song in the queue with the matchin spotify code
        AssertionError if the ip has already downvoted
        :param code: spotify code of song to downvote
        :param ip: ip of user who downvoted this song
        :return:
        """
        idx = self.queue.index(Song(code, 0, 0))
        song = self.queue[idx]
        assert (ip not in song.get_downvoted())  # No duplicate downvotes
        if ip in song.get_upvoted():             # User cannot upvote and downvote
            song.remove_upvoted(ip)
        song.downvote(ip)
        self.update()

    def update(self):
        """
        Updates the queue when a song is added
        :return:
        """
        self.queue.sort(reverse=True)

    def get_queue(self):
        """
        Returns the queue
        :return: the song queue data structure
        """
        return self.queue


def test():
    testQueue = SongQueue()

    # Try to add songs, should succeed
    try:
        print("Adding some songs")
        testQueue.add("A", 0)
        testQueue.add("B", 0)
        testQueue.add("C", 0)
        testQueue.add("D", 0)
        print(testQueue)
    except:
        print("Failed to add unique songs.  Something must be wrong...")

    # Try to add duplicate song, should fail
    try:
        testQueue.add("A", 0)
    except:
        print("Successfully restricted user from adding duplicate song")

    # Try to add upvotes to songs
    try:
        print("\nAdding some upvotes")
        testQueue.upvote("A", 1)
        testQueue.upvote("B", 1)
        testQueue.upvote("D", 1)

        testQueue.upvote("D", 2)
        testQueue.upvote("B", 2)
        testQueue.upvote("A", 2)

        testQueue.upvote("D", 3)
        testQueue.upvote("B", 3)

        testQueue.upvote("C", 4)
        testQueue.upvote("D", 4)
        testQueue.upvote("A", 4)
        print(testQueue)
    except:
        print("Failed to upvote songs.  Something must be wrong...")

    # Try to upvote song again, should fail
    try:
        testQueue.upvote("A", 0)
    except:
        print("Successfully restricted user from upvoting doubly")

    # Attempt to allow user to downvote a song after upvoting it
    try:
        print("\nChanging user 1 from upvote to downvote")
        testQueue.downvote("A", 1)
        print(testQueue)
    except:
        print("Failed to change user vote.  Something must be wrong...")

    # Attempt to doubly downvote
    try:
        testQueue.downvote("A", 1)
        print(testQueue)
    except:
        print("Successfully restricted user from downvoting doubly")


test()
