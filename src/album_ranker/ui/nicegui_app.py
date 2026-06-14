"""
UI module in NiceGUI
"""

from nicegui import ui

@ui.page("/")
def homepage():
    ui.label("Hello, welcome to the Album Ranker!")
    ui.link("Continue", "/rank_session")

@ui.page("/rank_session")
def rank_session():
    ui.label("Ranking goes here")

ui.run()