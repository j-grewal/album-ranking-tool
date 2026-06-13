"""
Main coding block
"""

import cli
import csv_io

def main():
    filepath = "data/example.csv"
    list_of_albums = csv_io.list_of_dicts_to_albums(csv_io.csv_to_list_of_dicts(filepath))
    print(list_of_albums)
    print(len(list_of_albums))
    for i in range(0, 4):
        print(list_of_albums[i].title)
        print(list_of_albums[i].artist)
        print(list_of_albums[i].metadata)


if __name__ == "__main__":
    main()