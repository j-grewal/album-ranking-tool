"""
Main exeution module
"""

import logging

import cli
import csv_io
import ranking


logger = logging.getLogger(__name__)

def main():
    filepath = "src/album_ranker/data/example_small.csv"
    list_of_albums = csv_io.list_of_dicts_to_albums(csv_io.csv_to_list_of_dicts(filepath))

    if len(list_of_albums) == 0:
        print("CSV file did not contain any rows")
        return

    algorithm = ranking.BinaryInsertionSort(list_of_albums)
    session = ranking.RankingSession(algorithm)

    while not session.is_complete():
        # get next comparison pairs
        album_a, album_b = session.get_next_comparison()

        # get user choice
        choice = cli.get_user_choice(album_a, album_b)

        if choice == album_a:
            session.record_choice(album_a, album_b)
        elif choice == album_b:
            session.record_choice(album_b, album_a)

    print("Ranking complete :)")
    csv_io.list_of_albums_to_csv(session.get_ranking())

if __name__ == "__main__":
    main()
