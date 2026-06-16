"""
UI module in NiceGUI
"""

from nicegui import ui

@ui.page("/")
def homepage():
    ui.label("Hello, welcome to the Album Ranker!")
    with ui.link(target="/rank_session"):
        ui.button("Continue")

@ui.page("/rank_session")
def rank_session():
    ui.label("Ranking goes here")




ui.run()