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

- **requirements.txt** - Lists Python dependencies

## Installation
Clone the repository, navigate into the project folder, install dependencies, run the application:

```bash
git clone https://github.com/denisavdicc/dna-gene-scanner.git
cd dna-gene-scanner
pip install -r requirements.txt
python project.py
```
## Testing
Run automated tests to verify functionality:

```bash
pytest test_project.py
```
## Usage
1. Enter a DNA sequence in the input box
2. Click **Scan Sequence**
3. Matching genes and similarity scores will appear in the results box
