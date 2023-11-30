from tkinter import *
from tkinter import ttk
from openai import OpenAI

# client = OpenAI()

root = Tk()
root.grid_columnconfigure(0, weight = 0)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 0)
root.grid_rowconfigure(1, weight = 1)
root.attributes('-fullscreen', False)

frm = ttk.Frame(root, padding=10)
frm.grid()

def create_label(input_text, row):
    label = ttk.Label(frm, text=input_text, font=("Arial", 25), wraplength=1000, justify=LEFT)
    label.grid(column = 0,
               row = row,
               sticky = NW)

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()

string_thing = ""

def keystroke(event):
    global string_thing
    key = event.char
    print(f"'{key}' key pressed")
    # clear_frame()
    # string_thing = string_thing + key
    # string_thing = string_thing + key
    string_thing = string_thing + key
    create_label(string_thing, 0)

root.bind('<Key>', keystroke)

def main():
    print("hehe")    # text = ttk.Label(frm, text=key,font=("Arial", 25)).grid(column=0, row=0)

create_label("", 10) # Placeholder before user starts typing
create_label("ChatGPT (Chat Generative Pre-trained Transformer) is a large language model-based chatbot developed by OpenAI and launched on November 30, 2022, that enables users to refine and steer a conversation towards a desired length, format, style, level of detail, and language. Successive prompts and replies, known as prompt engineering, are considered at each conversation stage as a context.", 1)
restart = ttk.Button(frm, text="Restart", command=main)
restart.grid()
quit = ttk.Button(frm, text="Quit", command=quit)
quit.grid()
    
main()
root.mainloop()