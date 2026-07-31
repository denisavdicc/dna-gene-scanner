# DNA Gene Scanner
 
## Description
The DNA Gene Scanner is a Python application designed to compare a user-provided DNA sequence against a reference database of genes stored locally in `genes.txt`. The program utilizes a graphical interface built with Tkinter and employs fuzzy string matching to identify sequences that meet or exceed a specified similarity threshold.
It helps users find potential matches between their DNA sequences and known genes, showing a similarity score for each match. This tool is intended for educational and research purposes in computational biology and bioinformatics.
 
## Features
- Graphical User Interface using Tkinter
- Input field for DNA sequences
- Reads gene data from `genes.txt`, formatted as `GeneName: DNASequence`
- Compares sequences using Python's `difflib.SequenceMatcher` to calculate similarity ratios
- Adjustable match threshold (default 85%)
- Displays all matching genes with similarity percentages or a message indicating no matches found
- Error handling for missing input or failure to read the gene file
## File Structure
- **project.py** – Contains the main application and the following functions:
    - `main()` – Initializes the GUI and manages the application lifecycle
    - `read_genes_from_file()` – Reads and parses the gene database
    - `find_matches()` – Compares user-provided sequences against stored genes
    - `display_results()` – Formats the results for display
    - `scan_sequence()` – Handles getting the sequence from the user, finding matches and showing the results
- **test_project.py** – Contains unit tests for:
    - `read_genes_from_file()`
    - `find_matches()`
    - `display_results()`
- **genes.txt** – Database file containing gene names and sequences
- **requirements.txt** – Lists Python dependencies (`pytest`, used for running the test suite; `tkinter` and `difflib` are part of Python's standard library and don't need to be installed separately)
## Setup and Installation
 
**Important:** always run the commands below from inside the project folder (the one containing `project.py`). The app looks for `genes.txt` in your current folder, so running it from anywhere else will cause a "file not found" error.
 
### macOS
 
```bash
# 1. Clone the repository
git clone https://github.com/denisavdicc/dna-gene-scanner.git
cd dna-gene-scanner
 
# 2. Create a virtual environment (use Python 3.12)
python3.12 -m venv .venv
 
# 3. Activate it
source .venv/bin/activate
 
# 4. Install dependencies
pip install -r requirements.txt
 
# 5. Run the app
python3.12 project.py
```
 
If Python 3.12 isn't installed:
```bash
brew install python@3.12
```
 
**If the GUI window opens with missing or invisible elements:** this is a known bug in the outdated Tcl/Tk version bundled with Apple's system Python, not an issue with the app itself. Fix it by installing proper Tk support via [Homebrew](https://brew.sh):
```bash
brew install python-tk@3.12
```
 
### Windows
 
```bash
# 1. Clone the repository
git clone https://github.com/denisavdicc/dna-gene-scanner.git
cd dna-gene-scanner
 
# 2. Create a virtual environment
python -m venv .venv
 
# 3. Activate it
.venv\Scripts\activate
 
# 4. Install dependencies
pip install -r requirements.txt
 
# 5. Run the app
python project.py
```
 
If `python` isn't recognized, try `py` instead (`py -m venv .venv`, then `py project.py`) — this depends on how Python was installed on your machine.
 
## Testing
With the virtual environment activated, run:
```bash
pytest test_project.py
```
 
## Usage
1. Enter a DNA sequence in the input box
2. Click **Scan Sequence**
3. Matching genes and similarity scores will appear in the results box
