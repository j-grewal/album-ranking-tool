"""
UI module in NiceGUI
"""

import logging

from nicegui import ui, events

logger = logging.getLogger(__name__)

@ui.page("/")
def page_homepage():
    ui.label("Hello, welcome to the Album Ranker!")
    with ui.link(target="/csv_upload"):
        ui.button("Continue")

@ui.page("/csv_upload")
def page_csv_upload():
    upload = ui.upload(
        multiple=False,
        max_files=1,
        on_upload=handle_upload,
        on_rejected=ui.notify("Please upload a single CSV file"),
        auto_upload=True,
    ).props("accept=.csv")

@ui.page("/rank_session")
def page_rank_session():
    ui.label("Ranking goes here")

async def handle_upload(event: events.UploadEventArguments):
    logger.info(f"File uploaded: {event.file.name}, type: {event.file.content_type}")

    filename = event.file.name.lower()

    if not filename.endswith(".csv"):
        ui.notify("Please upload a csv file", color="red", type="negative")
    else:
        file_content_json = event.file.text()
        with ui.link(target="/rank_session"):
            ui.button("Continue")

ui.run()