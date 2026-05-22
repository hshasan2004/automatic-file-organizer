# Automatic File Organizer

A real-time automatic file organizer built with Python.  
This application monitors the Downloads folder and automatically organizes files into categorized folders based on file extensions.

---

## Features

- Real-time file monitoring using Watchdog
- Automatic file organization
- Duplicate-safe file renaming
- Automatic folder creation
- Unknown file support (`Others` folder)
- Standalone EXE support using PyInstaller
- Portable across different PCs
- Automatic Downloads folder detection

---

## File Categories

The organizer currently supports:

| Category | Extensions |
|---|---|
| Images | .jpg, .jpeg, .png, .gif |
| Audio | .mp3, .wav |
| Videos | .mp4, .mkv |
| PDFs | .pdf |
| Documents | .doc, .docx, .txt |
| Archives | .zip, .rar |
| Python Files | .py |

Unknown files are automatically moved to the `Others` folder.

---

## Technologies Used

- Python
- Watchdog
- PyInstaller
- pathlib
- shutil
- os

---

## Project Structure

```text
file_organizer/
│
├── main.py
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/automatic-file-organizer.git
```

### Move Into Project Folder

```bash
cd automatic-file-organizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

The application will start monitoring the Downloads folder automatically.

---

## Build EXE File

```bash
pyinstaller --onefile main.py
```

For silent background execution:

```bash
pyinstaller --onefile --noconsole main.py
```

---

## How It Works

1. The application monitors the Downloads folder in real time.
2. When a new file is detected:
   - file type is identified
   - matching category folder is selected
   - duplicate names are handled safely
   - file is moved automatically

---

## Duplicate File Handling

If a file with the same name already exists, the organizer automatically renames the new file.

Example:

```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

---

## Future Improvements

- Keyword-based smart sorting
- Notification popups
- GUI interface
- Logging system
- Custom user rules
- Multiple folder monitoring
- System tray support

---

## Author

Mohammad Hasan  
Email: hshasan2004@gmail.com

---

## License

This project is licensed under the MIT License.