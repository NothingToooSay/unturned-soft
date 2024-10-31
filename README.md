# Unturned Instant Exit Tool

## Description
This tool, written in Python, is designed for the game "Unturned." It allows players to instantly minimize the game when there is a delay in exiting, especially if it exceeds 1 minute on the server. This can be useful for preventing time loss and improving the gaming experience.

## Installation

### Required Libraries
To run the application, you need to install a few libraries. Execute the following command in your terminal:

```bash
pip install psutil keyboard
```
## Cloning the Repository
### First, clone the repository:

```bash
git clone <repository_URL>
cd <repository_folder_name>
```
## Setting Up a Virtual Environment (Optional)
It is recommended to create a virtual environment for isolating dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
```
## Usage
1. Run the script that monitors the game's state.
2. If the "Unturned" game is running and there is a delay in exiting that exceeds 1 minute, press the F10 key to instantly minimize the game.

## Notes
1. Make sure you have sufficient permissions to terminate processes.
2. If you encounter access issues, run the script as an administrator.


