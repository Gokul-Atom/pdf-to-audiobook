import sys
from tkinter import Tk, filedialog, Label, Button, Frame, ttk, Text, END, Scrollbar
from PyPDF2 import PdfReader
from threading import Thread
import pyttsx3

root = Tk()
BG_COLOR = "#404040"
root.resizable(False, False)
root.title("PDF to Audiobook")
root.config(bg=BG_COLOR)
mainframe = Frame(root, bg=BG_COLOR)

engine = pyttsx3.init()
voices = engine.getProperty("voices")
voice_names = [voice.name for voice in voices]
voice_ids = [voice.id for voice in voices]
engine.setProperty("voice", voices[0].id)

filename = None
content = None
pdf_filetype = dict(defaultextension=".pdf", filetypes=[("pdf files", "*.pdf")])


def voice_select(e):
    voice_id = voice_names.index(combo_engine_select.get())
    engine.setProperty("voice", voice_ids[voice_id])


def sample_voice():
    engine.say("This is the sample demo of my voice")
    engine.runAndWait()


def play_demo():
    thread = Thread(target=sample_voice)
    thread.start()


def open_file():
    global filename
    filename = filedialog.askopenfile(**pdf_filetype).name
    if filename.split(".")[-1].lower() == "pdf":
        label_filename.config(text=filename)
        button_save.grid_forget()
        button_extract_file.grid(row=5, column=0, columnspan=4, pady=(0, 8))
    else:
        label_filename.config(text="This is not a pdf file")


def extract_text():
    global content
    text_content.replace(1.0, END, "")
    reader = PdfReader(filename)
    pages = len(reader.pages)
    content = ""
    for page in range(pages):
        content += reader.pages[page].extract_text()
    text_content.insert(1.0, content)
    if content:
        button_extract_file.grid(row=5, column=0, columnspan=2)
        button_save.grid(row=5, column=2, columnspan=2, pady=(0, 8))


def save():
    save_filename = filedialog.asksaveasfilename(initialfile="Untitled", defaultextension=".pdf", filetype=[("Audio files", ".mp3")])
    engine.save_to_file(text_content.get(1.0, END), filename=save_filename)
    engine.runAndWait()


button_play_demo = Button(mainframe, text="     >️", command=play_demo, fg="green", width=2, height=1, font=("", 14, "bold"))
button_open = Button(mainframe, text="Open File", command=open_file, font=("", 14, "bold"))
button_extract_file = Button(mainframe, text="Extract Text", command=extract_text, font=("", 14, "bold"))
button_save = Button(mainframe, text="Save Audiobook", command=save, font=("", 14, "bold"))

combo_engine_select = ttk.Combobox(mainframe, state="readonly", values=voice_names, width=55, font=("", 14))
combo_engine_select.set(voice_names[0])
combo_engine_select.bind("<<ComboboxSelected>>", voice_select)

label_voice_engine = Label(mainframe, text="Choose Voice Engine", bg=BG_COLOR, fg="white", font=("", 14, "bold"))
label_filename = Label(mainframe, bg=BG_COLOR, fg="white", font=("", 14))

text_content = Text(mainframe, bg="#303030", fg="white", insertbackground="red")

scrollbar = Scrollbar(mainframe, command=text_content.yview, width=20)
text_content.config(yscrollcommand=scrollbar.set)

mainframe.grid(row=0, column=0, padx=20, pady=20)
label_voice_engine.grid(row=0, column=0, columnspan=4)
combo_engine_select.grid(row=1, column=1, columnspan=3, sticky="EW")
button_play_demo.grid(row=1, column=0)
button_open.grid(row=3, column=0, columnspan=4)
label_filename.grid(row=4, column=0, columnspan=4, sticky="EW")
text_content.grid(row=6, column=0, columnspan=3, sticky="NSEW")
scrollbar.grid(row=6, column=3, sticky="NS")

root.bind("<Escape>", sys.exit)
root.eval("tk::PlaceWindow . center")
root.mainloop()
