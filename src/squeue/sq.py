
from serial.serialize import Serializable

class SongQueue():

    def __init__(self):
        self.queue = []

    def peek(self):
        """
        Finds the queue element with the highest voted
        :return: tuple with maximum priority key/value pair
        """
        return self.queue[0]

    def pop(self):
        """
        Removes the song with the highest rating
        :return: the spotify song code of the removed song
        """
        return 0

    def add(self, code):
        """
        Adds a new song to the queue
        :param code: spotify code of song to add
        """
        pass

    def remove(self, code):
        """
        Removes a song from the queue
        :param code: spotify code of song to remove
        """
        pass

    def upvote(self, code):
        """
        Upvotes the song in the queue with the matchin spotify code
        :param code:
        :return:
        """

    def downvote(self, code):
        """
        Downvotes the song in the queue with the matchin spotify code
        :param code:
        :return:
        """

    def get_queue(self):
        """
        Returns the queue
        :return:
        """
        return self.queue
