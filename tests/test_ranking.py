"""
Test module for ranking.py
"""

import pytest

import src.album_ranker.ranking as rank

@pytest.fixture
def single_album_algo(single_album_array):
    algo = rank.BinaryInsertionSort(single_album_array)
    return algo

@pytest.fixture
def empty_album_algo(empty_album_array):
    algo = rank.BinaryInsertionSort(empty_album_array)
    return algo

@pytest.fixture
def single_album_session(single_album_algo):
    session = rank.RankingSession(single_album_algo)
    return session

@pytest.fixture
def empty_album_session(empty_album_algo):
    session = rank.RankingSession(empty_album_algo)
    return session
    
def test_single_album_session_complete(single_album_session):
    assert single_album_session.is_complete() == True

def test_empty_album_session_complete(empty_album_session):
    assert empty_album_session.is_complete() == True



# tests to implement:
# Check insertion works correctly
