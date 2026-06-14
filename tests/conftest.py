"""
Fixtures for tests
"""

import pytest

from src.album_ranker.album import Album

@pytest.fixture
def single_album_array():
    array = [Album("Melodrama", "Lorde", {"Year Released": "2017"})]
    return array

@pytest.fixture
def empty_album_array():
    return []