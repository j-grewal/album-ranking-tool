"""
Module to handle reading and writing csv files
"""

from csv import DictReader, DictWriter
from models import Album

def csv_to_list_of_dicts(filepath):
    list_of_dicts = []
    with open(filepath, newline='') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            row_dict = {}
            row_dict["title"] = row["title"]
            row_dict["artist"] = row["artist"]
            metadata = {}
            for key in row.keys():
                if key == "title" or key == "artist":
                    continue
                else:
                    metadata[key] = row[key]
            
            row_dict["metadata"] = metadata

            list_of_dicts.append(row_dict)

    return list_of_dicts


def list_of_dicts_to_albums(listofdicts):
    list_of_albums = []
    for d in listofdicts:
        list_of_albums.append(
            Album(
                d["title"],
                d["artist"],
                d["metadata"],
            )
        )

    return list_of_albums


def list_of_albums_to_csv(listofalbums):
    pass

