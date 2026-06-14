"""
Module for handling ranking logic
"""

import logging
from random import randint

logger = logging.getLogger(__name__)

class RankingAlgorithm:

    def __init__(self, album_list):
        self.album_list = album_list
        self.current_ranking = [album_list[-1]]
        self.unranked_albums = album_list.copy()[:-1]

    def is_complete(self):
        if len(self.unranked_albums) > 0:
            return False
        else:
            return True

    def get_ranking(self):
        return self.current_ranking


class BinaryInsertionSort(RankingAlgorithm):

    def __init__(self, album_list):
        super().__init__(album_list)
        self.low_index = 0
        self.high_index = len(self.current_ranking) - 1
        self.middle_index = (self.high_index + self.low_index) // 2
        self.current_album = self.unranked_albums[0]

    def get_next_comparison(self):
        return self.current_album, self.current_ranking[self.middle_index]
    
    def record_choice(self, winner, loser):
        logger.info(f"{winner.title} beat {loser.title}")
        if self.current_album == winner:
            self.high_index = self.middle_index - 1
        elif self.current_album == loser:
            self.low_index = self.middle_index + 1

        self.middle_index = (self.high_index + self.low_index) // 2

        # Check if we are at insertion index
        if self.high_index < self.low_index:
            self.insert_current_album(self.low_index)

            # Check if we have finished ranking
            if not self.is_complete():
                self.set_next_album_to_insert()

    def insert_current_album(self, index):
        left = self.current_ranking[0:index]
        right = self.current_ranking[index:]
        left.append(self.current_album)
        self.current_ranking = left + right
        logger.info(f"{self.current_album.title} has been inserted: {self.get_current_ranking_titles()}")
        self.unranked_albums.pop(0)

    def set_next_album_to_insert(self):
        self.current_album = self.unranked_albums[0]
        self.low_index = 0
        self.high_index = len(self.current_ranking) - 1
        self.middle_index = (self.high_index + self.low_index) // 2

    def skip_comparison(self):
        self.middle_index = randint(self.low_index, self.high_index)

    def get_current_ranking_titles(self):
        rank_titles = []
        for album in self.current_ranking:
            rank_titles.append(album.title)
        return rank_titles


class RankingSession:

    def __init__(self, algorithm=BinaryInsertionSort()):
        self.algorithm = algorithm
        self._skipped_comparisons = []
        self._removed_albums = []
        self._comparison_history = []

    def get_next_comparison(self):
        return self.algorithm.get_next_comparison()

    def get_ranking(self):
        return self.algorithm.current_ranking

    def record_choice(self, winner, loser):
        self._comparison_history.append((winner, loser))
        self.algorithm.record_choice(winner, loser)

    def skip_comparison(self, album_a, album_b):
        self._skipped_comparisons.append((album_a, album_b))
        self.algorithm.skip_comparison()

    def has_comparison_been_made(self, album_a, album_b):
        if (album_a, album_b) in self._comparison_history or (album_b, album_a) in self._comparison_history:
            return True
        else:
            return False
    
    def has_comparison_been_skipped(self, album_a, album_b):
        if (album_a, album_b) in self._skipped_comparisons or (album_b, album_a) in self._skipped_comparisons:
            return True
        else:
            return False

    def is_complete(self):
        return self.algorithm.is_complete()
    
    def undo_choice(self):
        self._comparison_history.pop()
        # Would also need to set the state to the previous comparison too (which can be gotten from the pop)
        # Would also need to reverse any ranking updates that were made as a result of the previous choice (this may be tricky)




# Make sure that editing these lists of albums is handled copmletely by the class so that if an album is added to the current rankings, it can be removed from the unrakned albums in the same funciton call.
