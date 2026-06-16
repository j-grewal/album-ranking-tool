"""
UI module in NiceGUI
"""

from nicegui import ui, events

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
    )

@ui.page("/rank_session")
def page_rank_session():
    ui.label("Ranking goes here")

def handle_upload(event: events.UploadEventArguments):
    print(f"File uploaded: {event.file.name}, type: {event.file.content_type}")
    if event.file.content_type == "text/csv":
        file_content_json = event.file.json()
        with ui.link(target="/rank_session"):
            ui.button("Continue")
    else:
        ui.notify("Please upload a csv file", color="red")

ui.run()