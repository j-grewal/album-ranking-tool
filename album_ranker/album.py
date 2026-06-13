"""
Classes for the project
"""

# This could be a dataclass
class Album:
    """
    Album class to store the attributes of each album
    """

    def __init__(self, title, artist, metadata):
        self.title = title
        self.artist = artist
        self.metadata = metadata
