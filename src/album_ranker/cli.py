"""
Module for handling the command line user interface
"""

def get_csv_filepath():
    filepath = input("Please enter the filepath of your csv file:\n")
    return filepath

def get_user_choice(album_a, album_b):
    choice = input(f"Which album do you prefer, {album_a.title} or {album_b.title}? Enter 1 for {album_a.title} or 0 for {album_b.title}.\n")
    while choice != "1" and choice != "0":
        choice = input(f"Invalid choice. Please enter 1 for {album_a.title} or 0 for {album_b.title}.\n")
    
    if choice == "1":
        return album_a
    elif choice == "0":
        return album_b
