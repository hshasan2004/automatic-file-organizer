# Automatic File Organizer

> A real-time intelligent file organization system built with Python.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Watchdog](https://img.shields.io/badge/Watchdog-File_Monitoring-green)
![Automation](https://img.shields.io/badge/Automation-Enabled-purple)
![Windows](https://img.shields.io/badge/Windows-Supported-00A8FF)
![License](https://img.shields.io/badge/License-MIT-yellow)

![Repo Size](https://img.shields.io/github/repo-size/hshasan2004/Automatic-File-Organizer)
![Last Commit](https://img.shields.io/github/last-commit/hshasan2004/Automatic-File-Organizer)
![Stars](https://img.shields.io/github/stars/hshasan2004/Automatic-File-Organizer)
![Forks](https://img.shields.io/github/forks/hshasan2004/Automatic-File-Organizer)
![Issues](https://img.shields.io/github/issues/hshasan2004/Automatic-File-Organizer)

---

## Overview

Automatic File Organizer continuously monitors the Downloads folder and automatically sorts files into categorized folders based on their extensions.

The project is designed to simplify file management, reduce desktop clutter, and improve productivity through real-time automation.

---

## Features

- Real-time file monitoring using Watchdog
- Automatic file categorization
- Duplicate-safe file renaming
- Automatic folder creation
- Unknown file handling (`Others` folder)
- Portable executable support with PyInstaller
- Cross-device portability
- Automatic Downloads folder detection
- Lightweight and fast execution

---

## Supported File Categories

| Category | Extensions |
|---|---|
| Images | `.jpg` `.jpeg` `.png` `.gif` |
| Audio | `.mp3` `.wav` |
| Videos | `.mp4` `.mkv` |
| PDFs | `.pdf` |
| Documents | `.doc` `.docx` `.txt` |
| Archives | `.zip` `.rar` |
| Python Files | `.py` |

Unknown files are automatically moved into the `Others` folder.

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

### Navigate to Project Directory

```bash
cd automatic-file-organizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python main.py
```

The application will automatically start monitoring the Downloads folder in real time.

---

## Build Executable File

### Standard EXE

```bash
pyinstaller --onefile main.py
```

### Silent Background EXE

```bash
pyinstaller --onefile --noconsole main.py
```

---

## How It Works

1. The application monitors the Downloads folder continuously.
2. When a new file is detected:
   - The file extension is identified
   - A matching category folder is selected
   - Duplicate filenames are handled safely
   - The file is automatically moved

---

## Duplicate File Handling

If a file with the same name already exists, the organizer automatically renames the new file.

### Example

```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

---

## Future Improvements

- Smart keyword-based sorting
- Desktop notifications
- GUI interface
- Activity logging system
- Custom user-defined rules
- Multiple folder monitoring
- System tray integration

---

## Author

**Mohammad Hasan**  
📧 hshasan2004@gmail.com

---

## License

This project is licensed under the MIT License.
