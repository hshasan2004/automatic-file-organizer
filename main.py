import os
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from pathlib import Path

MAIN_FOLDER = str(Path.home() / "Downloads")

TEMP_EXTENSIONS = [".crdownload", ".tmp", ".part"]

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt"],
    "Archives": [".zip", ".rar"],
    "Python": [".py"],
}


def get_unique_name(destination_path):

    if not os.path.exists(destination_path):
        return destination_path

    folder_path = os.path.dirname(destination_path)

    file_name = os.path.basename(destination_path)

    name, ext = os.path.splitext(file_name)

    count = 1

    while os.path.exists(destination_path):

        new_name = f"{name}_{count}{ext}"

        destination_path = os.path.join(folder_path, new_name)

        count += 1

    return destination_path


def move_file(source_path, folder_path, file):

    if not os.path.exists(source_path):
        return

    os.makedirs(folder_path, exist_ok=True)

    destination_path = os.path.join(folder_path, file)

    destination_path = get_unique_name(destination_path)

    try:

        shutil.move(source_path, destination_path)

        final_name = os.path.basename(destination_path)

        print(f"Moved {final_name} to {os.path.basename(folder_path)} folder")

    except Exception as e:

        print(f"Error moving file: {e}")

def organize_file(file_path):

    file = os.path.basename(file_path)

    if os.path.isdir(file_path):
        return

    extension = os.path.splitext(file)[1].lower()

    if extension in TEMP_EXTENSIONS:
        return

    moved = False

    for folder_name, extensions in file_types.items():

        if extension in extensions:

            folder_path = os.path.join(MAIN_FOLDER, folder_name)

            move_file(file_path, folder_path, file)

            moved = True

            break

    if not moved:

        others_folder = os.path.join(MAIN_FOLDER, "Others")

        move_file(file_path, others_folder, file)


class MyHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        time.sleep(2)

        organize_file(event.src_path)


    def on_moved(self, event):

        if event.is_directory:
            return

        time.sleep(2)

        organize_file(event.dest_path)


event_handler = MyHandler()

observer = Observer()

observer.schedule(event_handler, MAIN_FOLDER, recursive=False)

observer.start()

print("Watching folder...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:

    observer.stop()

observer.join()