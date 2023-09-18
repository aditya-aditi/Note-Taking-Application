import customtkinter as ctk
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['note_taking_application']
collection = db['notes']


def add_note():

    # Check if the entry are empty
    title = title_ent.get()
    note = textbox_txt.get("1.0", ctk.END)
    print(note)
    if title == "":
        addNote_btn.configure(text = "Please enter a title")
    elif note == "\n":
        addNote_btn.configure(text = "Please enter a note")
    else:
        addNote_btn.configure(text = "Add Note")
        collection.insert_one({"title": title, "note": note})




# todo: add a button to delete notes

def view_notes():
    view_window = ctk.CTk()
    view_window.geometry("600x450")
    view_window.title("View Notes")

    scrollable_frame = ctk.CTkScrollableFrame(view_window, width=600, height=450)
    scrollable_frame.pack()

    # Fetch and display notes from the database
    notes = collection.find()
    for note in notes:
        # Seperator
        seperator_lbl = ctk.CTkLabel(scrollable_frame, text="----"*500)
        seperator_lbl.pack()

        # Displays the note title
        notes_title = ctk.CTkEntry(scrollable_frame, width=300, border_width=2)
        notes_title.insert(1, f"{note['title']}")
        notes_title.pack(pady=20)
        notes_title.configure(state="disabled")

        #Displays the note content
        notes_content = ctk.CTkTextbox(scrollable_frame, width=300, border_width=2)
        notes_content.insert(ctk.END, f"{note['note']}")
        notes_content.pack(pady=20)
        notes_content.configure(state="disabled")

    view_window.resizable(False, False)
    view_window.mainloop()


# Window
if __name__ == '__main__':
    window = ctk.CTk()
    window.geometry("600x450")

    # window.grid_rowconfigure(1, weight=0)

    title_ent = ctk.CTkEntry(master=window, placeholder_text="Note Title", width=450, height=35)
    title_ent.pack(pady=50)

    textbox_txt = ctk.CTkTextbox(window, width=450, border_width=2)
    textbox_txt.pack()

    addNote_btn = ctk.CTkButton(window, text="Add Note", command=add_note)
    addNote_btn.pack(pady=8)

    viewNote_btn = ctk.CTkButton(window, text="View Note", command=view_notes)
    viewNote_btn.pack(pady=8)

    window.resizable(False, True)
    window.mainloop()
