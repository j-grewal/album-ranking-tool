"""
Test module for ranking.py
"""

import pytest

import src.album_ranker.ranking as rank

@pytest.fixture
def single_album_session(single_album_array):
    algo = rank.BinaryInsertionSort(single_album_array)
    session = rank.RankingSession(algo)
    return session


def test_single_album_session(single_album_session):
    assert single_album_session.is_complete() == True


# tests to implement:
# Empty album list
# One-entry album list
# Check insertion works correctly
