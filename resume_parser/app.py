import tkinter
import PyPDF2
from tkinter.filedialog import askopenfile
from converter import convert
from PIL import Image,ImageTk
from main import main

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=600, height=100)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open(r'.\resume_parser\pics\logo-no-background.png')
logo = ImageTk.PhotoImage(logo)

w = tkinter.Label(root, image=logo)
w.place(x=425,y=275)


#instructions
instructions = tkinter.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.place(x=740,y=650)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        page_content = convert(page_content)
        browse_text.set("Browse")
        print(page_content)
        main(page_content)
    
#browse button
browse_text = tkinter.StringVar()
browse_btn = tkinter.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.place(x=850,y=700)

#canvas = tkinter.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.attributes('-fullscreen', True)
root.mainloop()