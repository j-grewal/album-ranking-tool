"""
Classes for the project
"""
class Album:
    """
    Album class to store the attributes of each album
    """

    def __init__(self, title, artist, metadata):
        self.title = title
        self.artist = artist
        self.metadata = metadata

class RankingSession:

    def __init__(self, albums, sort_algo):
        self.albums = albums
        self.current_ranking = []
        self.unranked_albums = albums.copy()
        self.skipped_albums = []
        self.removed_albums = []
        self.comparison_history = []
        self.sort_algo = sort_algo
        self.session_complete = False

    def record_choice(self, winner, loser):
        self.comparison_history.append((winner, loser))
        pass

    def is_complete(self):
        return self.session_complete
    
    def finish(self):
        self.session_complete == True

    def undo_choice(self):
        self.comparison_history.pop()
        # Would also need to set the state to the previous comparison too (which can be gotten from the pop)
        # Would also need to reverse any ranking updates that were made as a result of the previous choice (this may be tricky)




# Make sure that editing these lists of albums is handled copmletely by the class so that if an album is added to the current rankings, it can be removed from the unrakned albums in the same funciton call.

