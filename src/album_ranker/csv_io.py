"""
Module to handle reading and writing csv files
"""

import logging
import random

from csv import DictReader, DictWriter
from album import Album

logger = logging.getLogger(__name__)


class AlbumSource:
    def __init__(self):
        self.list_of_albums = []
        self.list_of_fields = []

    def list_of_albums_to_csv(self, ranked_albums):
        with open("src/album_ranker/output/output.csv", "w", newline='') as csvfile:
            writer = DictWriter(csvfile, fieldnames=self.list_of_fields)
            writer.writeheader()

            for album in ranked_albums:
                row = {}
                for key in album.metadata:
                    row[key] = album.metadata[key]

                row["title"] = album.title
                row["artist"] = album.artist
                writer.writerow(row)

class CSVAlbumSource(AlbumSource):
    def __init__(self, filepath:str):
        super().__init__()
        self.filepath = filepath

    def _read_list_of_fields(self):
        with open(self.filepath, newline='') as csvfile:
            reader = DictReader(csvfile)
            self.list_of_fields = reader.fieldnames
            logger.info(f"Read in {len(self.list_of_fields)} fields from CSV file")
            return self.list_of_fields

    def _validate_input(self, reader:DictReader):
        header = self._read_list_of_fields()
        if "title" in header and "artist" in header:
            return True
        else:
            return False
    
    def file_to_list_of_albums(self):
        with open(self.filepath, newline='') as csvfile:
            reader = DictReader(csvfile)

            if not self._validate_input(reader):
                logger.warning("User submitted csv file without 'title' and 'artist' fields")
                return

            for row in reader:
                metadata = {}
                for key in row.keys():
                    if key == "title" or key == "artist":
                        continue
                    else:
                        metadata[key] = row[key]

                self.list_of_albums.append(
                    Album(
                        row["title"],
                        row["artist"],
                        metadata,
                    )
                )
        
        logger.info(f"Read in {len(self.list_of_albums)} rows from CSV file")

        random.shuffle(self.list_of_albums) # Why not?

        return self.list_of_albums


"""
def text_to_list_of_dicts(text):
    list_of_dicts = []
    reader = DictReader(text.splitlines())
    for row in reader:
        # validate that the row has title and artist keys
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
    
    logger.info(f"Read in {len(list_of_dicts)} rows from CSV text")

    return list_of_dicts
"""

class TextAlbumSource(AlbumSource):
    def __init__(self, text:str):
        super().__init__()
        self.text = text

    def text_to_list_of_albums(self):
        reader = DictReader(self.text.splitlines())

        if not self._validate_input(reader):
            logger.warning("User submitted csv file without 'title' and 'artist' fields")
            return

        for row in reader:
            metadata = {}
            for key in row.keys():
                if key == "title" or key == "artist":
                    continue
                else:
                    metadata[key] = row[key]

            self.list_of_albums.append(
                Album(
                    row["title"],
                    row["artist"],
                    metadata,
                )
            )
        
        logger.info(f"Read in {len(self.list_of_albums)} rows from CSV text")

        random.shuffle(self.list_of_albums) # Why not?

        return self.list_of_albums
