import tkinter
from tkinter import messagebox
from difflib import SequenceMatcher

def read_genes_from_file():
    genes = {}
    try:
        with open("genes.txt", "r", encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if ":" in line:
                    name, sequence = line.split(":")
                    genes[name.strip()] = sequence.strip().upper()
    except Exception as error:
        messagebox.showerror("File Error", f"An error occurred: {error}")
    return genes

def find_matches(genes, user_sequence, threshold=0.85):
    user_sequence = user_sequence.upper()
    found_genes = []
    for name, sequence in genes.items():
        similarity = SequenceMatcher(None, sequence, user_sequence).ratio()
        if similarity >= threshold:
            found_genes.append((name, round(similarity * 100, 2)))
    return found_genes

def display_results(found_genes):
    if not found_genes:
        return "No matching genes found."
    result_lines = [f"{name} ({match}%)" for name, match in found_genes]
    return "Matching genes found:\n" + "\n".join(result_lines)

def scan_sequence():
    sequence = dna_entry.get("1.0", tkinter.END).strip()
    if not sequence:
        messagebox.showwarning("Input Missing", "Please enter a DNA sequence." )
        return
    genes = read_genes_from_file()
    if not genes:
        messagebox.showwarning("File Error", "Failed to load genes.txt.")
        return
    found = find_matches(genes, sequence)
    result_text = display_results(found)
    result_box.config(state=tkinter.NORMAL)
    result_box.delete("1.0", tkinter.END)
    result_box.insert(tkinter.END, result_text)
    result_box.config(state=tkinter.DISABLED)

def main():
    global window, dna_entry, result_box

    window = tkinter.Tk()
    window.title("DNA Gene Scanner")
    window.geometry("700x600")
    window.configure(bg="white")

    TITLE_FONT = ("Arial", 20, "bold")
    LABEL_FONT = ("Arial", 12)
    BUTTON_FONT = ("Arial", 12)
    TEXT_FONT = ("Arial", 10)

    tkinter.Label(window, text="DNA Gene Scanner", font=TITLE_FONT, bg="white", fg="black").pack(pady=10)
    tkinter.Label(window, text="Enter DNA Sequence:", font=LABEL_FONT, bg="white").pack(pady=(20, 5))
    dna_entry = tkinter.Text(window, height=5, width=80, font=TEXT_FONT, bd=2, relief=tkinter.GROOVE)
    dna_entry.pack()

    tkinter.Button(window, text="Scan Sequence", command=scan_sequence, font=BUTTON_FONT, bg="#0A78D2", fg="white", padx=10, pady=5).pack(pady=15)
    tkinter.Label(window, text="Results:", font=LABEL_FONT, bg="white").pack()
    result_box = tkinter.Text(window, height=12, width=80, font=TEXT_FONT, state=tkinter.DISABLED, bd=2, relief=tkinter.SUNKEN, bg="white")
    result_box.pack(pady=(5, 20))
    window.mainloop()

if __name__ == "__main__":
    main()