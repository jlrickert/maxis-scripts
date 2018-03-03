import tkinter as tk


def submit(*args):
    print(int(case_number[0].get()))
    print(str(case_note_file[0].get()))
    print(str(description[0].get()))
    print(str(worker_signature[0].get()))


root = tk.Tk()
root.title("Blank case notes")

mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

case_number = tk.IntVar(value=123),
case_note_file = tk.StringVar(),
description = tk.StringVar(),
worker_signature = tk.StringVar(value="Python was here"),

case_number_entry = tk.Entry(mainframe, width=21, textvariable=case_number)
case_number_entry.grid(row=1, column=2, sticky=(tk.N, tk.W))

case_note_file_entry = tk.Entry(
    mainframe, width=21, textvariable=case_note_file)
case_note_file_entry.grid(row=2, column=2, sticky=(tk.N, tk.W))

description_entry = tk.Entry(mainframe, width=21, textvariable=description)
description_entry.grid(row=3, column=2, sticky=(tk.N, tk.W))

worker_signature_entry = tk.Entry(
    mainframe, width=21, textvariable=worker_signature)
worker_signature_entry.grid(row=4, column=2, sticky=(tk.N, tk.W))

tk.Label(mainframe, text="Case number").grid(row=1, column=1, sticky=tk.W)
tk.Label(mainframe, text="Case note file").grid(row=2, column=1, sticky=tk.W)
tk.Label(mainframe, text="Description").grid(row=3, column=1, sticky=tk.W)
tk.Label(mainframe, text="Worker Signature").grid(row=4, column=1, sticky=tk.W)

tk.Button(
    mainframe, text="Submit", command=submit).grid(
        row=5, column=3, sticky=tk.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

case_number_entry.focus()
root.bind('<Return>', submit)

root.mainloop()
