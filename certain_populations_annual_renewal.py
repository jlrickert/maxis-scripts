"""
case number
date renewal recieve
interview data
interview type: drop box
shelter: drop box
shelter cost or n/a
how was shelter verified?
list assets
changes reported
worker signature
"""

import tkinter as tk


def submit():
    print("rawr")


root = tk.Tk()
root.title("Certain populations annual renewal")

mainframe = tk.Frame(root)
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.N, tk.E, tk.S))
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)

case_number = tk.IntVar()
date_renewal = tk.StringVar()
interview_data = tk.StringVar()
interview_type = tk.StringVar()
shelter = tk.StringVar()
shelter_cost = tk.IntVar()
shelter_verified = tk.StringVar()
assets = tk.StringVar()
reported_changes = tk.StringVar()
worker_signature = tk.StringVar()

case_number_entry = tk.Entry(mainframe, width=21, textvariable=case_number)
case_number_entry.grid(row=1, column=2, sticky=(tk.N, tk.W))

date_renewal_entry = tk.Entry(mainframe, width=21, textvariable=date_renewal)
date_renewal_entry.grid(row=2, column=2, sticky=(tk.N, tk.W))

interview_data_entry = tk.Entry(mainframe, width=21, textvariable=interview_data)
interview_data_entry.grid(row=3, column=2, sticky=(tk.N, tk.W))

interview_type_entry = tk.OptionMenu(mainframe, interview_type, "a", "b", "c")
interview_type_entry.grid(row=4, column=2, sticky=(tk.N, tk.W))

shelter_entry = tk.OptionMenu(mainframe, shelter, "a", "b", "c")
shelter_entry.grid(row=5, column=2, sticky=(tk.N, tk.W))

shelter_cost_entry = tk.OptionMenu(mainframe, shelter, "a", "b", "c")
shelter_cost_entry.grid(row=6, column=2, sticky=(tk.N, tk.W))

shelter_verified_entry = tk.Entry(mainframe, width=21, textvariable=shelter_verified)
shelter_verified_entry.grid(row=7, column=2, sticky=(tk.N, tk.W))

assets_entry = tk.Entry(mainframe, width=21, textvariable=assets)
assets_entry.grid(row=8, column=2, sticky=(tk.N, tk.W))

reported_changes_entry = tk.Entry(mainframe, width=21, textvariable=reported_changes)
reported_changes_entry.grid(row=9, column=2, sticky=(tk.N, tk.W))

worker_signature_entry = tk.Entry(
    mainframe, width=21, textvariable=worker_signature)
worker_signature_entry.grid(row=10, column=2, sticky=(tk.N, tk.W))


tk.Label(mainframe, text="Case number").grid(row=1, column=1, sticky=tk.W)
tk.Label(mainframe, text="Date renewal recieve").grid(row=2, column=1, sticky=tk.W)
tk.Label(mainframe, text="Interview Data").grid(row=3, column=1, sticky=tk.W)
tk.Label(mainframe, text="Interview type").grid(row=4, column=1, sticky=tk.W)
tk.Label(mainframe, text="Shelter").grid(row=5, column=1, sticky=tk.W)
tk.Label(mainframe, text="Shelter cost on n/a").grid(row=6, column=1, sticky=tk.W)
tk.Label(mainframe, text="How was shelter verified?").grid(row=7, column=1, sticky=tk.W)
tk.Label(mainframe, text="Assets").grid(row=8, column=1, sticky=tk.W)
tk.Label(mainframe, text="Changes reported").grid(row=9, column=1, sticky=tk.W)
tk.Label(mainframe, text="Worker signature").grid(row=10, column=1, sticky=tk.W)

tk.Button(
    mainframe, text="Submit", command=submit).grid(
        row=11, column=3, sticky=tk.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


case_number_entry.focus()
root.bind("<Return>", submit)
root.mainloop()
