from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from deep_translator import GoogleTranslator

root = Tk()
root.title("Language Translator")
root.geometry("1200x700")
root.resizable(False, False)

bg_image = Image.open("background.jpg")  
bg_image = bg_image.resize((1200, 700))
bg = ImageTk.PhotoImage(bg_image)

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title = Label(root, text="LANGUAGE TRANSLATOR",
              font=("Times New Roman", 28, "bold"),
              bg="#000000", fg="white")
title.pack(pady=10)

main_frame = Frame(root, bg="#000000")
main_frame.pack(pady=10)

input_frame = Frame(main_frame, bg="#000000")
input_frame.grid(row=0, column=0, padx=20)

Label(input_frame, text="Enter Text",
      font=("Arial", 20, "bold"),
      bg="#000000", fg="white").pack(pady=5)

Input_text = Text(input_frame, font=("Arial", 14),
                  height=12, width=40, wrap=WORD)
Input_text.pack()

scroll_in = Scrollbar(input_frame, command=Input_text.yview)
scroll_in.pack(side=RIGHT, fill=Y)
Input_text.config(yscrollcommand=scroll_in.set)

center_frame = Frame(main_frame, bg="#000000")
center_frame.grid(row=0, column=1, padx=20)

output_frame = Frame(main_frame, bg="#000000")
output_frame.grid(row=0, column=2, padx=20)

Label(output_frame, text="Output",
      font=("Arial", 20, "bold"),
      bg="#000000", fg="white").pack(pady=5)

Output_text = Text(output_frame, font=("Arial", 14),
                   height=12, width=40, wrap=WORD)
Output_text.pack()

scroll_out = Scrollbar(output_frame, command=Output_text.yview)
scroll_out.pack(side=RIGHT, fill=Y)
Output_text.config(yscrollcommand=scroll_out.set)

languages = [
    "auto", "english", "hindi", "french", "german",
    "spanish", "italian", "japanese", "korean", "chinese"
]

lang_frame = Frame(root, bg="#000000")
lang_frame.pack(pady=10)

src_lang = ttk.Combobox(lang_frame, values=languages, width=20)
src_lang.grid(row=0, column=0, padx=50)
src_lang.set("auto")

dest_lang = ttk.Combobox(lang_frame, values=languages, width=20)
dest_lang.grid(row=0, column=1, padx=50)
dest_lang.set("hindi")

def show_toast(message, color="#f44336"):
    toast = Label(root, text=message, font=("Arial", 14, "bold"), bg=color, fg="white", padx=20, pady=10, relief=RIDGE, bd=2)
    toast.place(relx=0.5, y=50, anchor=CENTER)
    toast.lift()
    root.after(3000, toast.destroy)

def Translate():
    try:
        text = Input_text.get(1.0, END).strip()
        src = src_lang.get()
        dest = dest_lang.get()

        if text == "":
            show_toast("Please enter text", "#ff9800")
            return

        translated = GoogleTranslator(source=src, target=dest).translate(text)

        Output_text.delete(1.0, END)
        Output_text.insert(END, translated)

    except Exception as e:
        show_toast(f"Error: {str(e)[:50]}...", "#f44336")


def Clear():
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)


def Swap():
    src = src_lang.get()
    dest = dest_lang.get()
    
    if src == "auto":
        src = "english"
        
    src_lang.set(dest)
    dest_lang.set(src)

button_frame = Frame(root, bg="#3C3838")
button_frame.pack(pady=20)

Button(button_frame, text="Translate",
       font=("Arial", 16, "bold"),
       bg="green", fg="white",
       width=12, command=Translate).grid(row=0, column=0, padx=10)

Button(button_frame, text="Clear",
       font=("Arial", 16, "bold"),
       bg="red", fg="white",
       width=12, command=Clear).grid(row=0, column=1, padx=10)

Button(button_frame, text="Swap 🔁",
       font=("Arial", 16, "bold"),
       bg="blue", fg="white",
       width=12, command=Swap).grid(row=0, column=2, padx=10)

footer = Label(root,
               text="Project by ArShx17",
               font=("Arial", 12),
               bg="#000000", fg="white")
footer.pack(side=BOTTOM, pady=10)

root.mainloop()