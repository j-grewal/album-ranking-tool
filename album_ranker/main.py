"""
Main coding block
"""

import logging

import csv_io
import ranking


logger = logging.getLogger(__name__)

def main():
    filepath = "data/example.csv"
    list_of_albums = csv_io.list_of_dicts_to_albums(csv_io.csv_to_list_of_dicts(filepath))
    
    algorithm = ranking.BinaryInsertionSort(list_of_albums)
    session = ranking.RankingSession(algorithm)

    while not session.is_complete():
        # get next comparison pairs
        # get user choice
        # record choice
        pass

# session.get_ranking()
# save ranking to csv

if __name__ == "__main__":
    main()