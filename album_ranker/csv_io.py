"""
Module to handle reading and writing csv files
"""

import logging

from csv import DictReader, DictWriter
from album_ranker.album import Album

logger = logging.getLogger(__name__)

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
    
    logger.info(f"Read in {len(list_of_dicts)} rows from CSV file")

    return list_of_dicts


def list_of_dicts_to_albums(listofdicts):
    list_of_albums = []
    logger.info(f"Converting list of dicts to a list of album objects")
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

