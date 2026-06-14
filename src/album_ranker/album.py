"""
Classes for the project
"""

from dataclasses import dataclass

@dataclass
class Album:
    """
    Album class to store the attributes of each album
    """
    title: str
    artist: str
    metadata: dict
