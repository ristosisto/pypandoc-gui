# have the user pick a file to be converted 
# have a dropbox list of options that allows the user to choose which file type to convert their og file to
# use pandoc to then do what the user chooses 

from tkinter import filedialog as fd
from tkinter import *
import os
import subprocess



#TODO make the options derived from the pandoc command 
#options_string = subprocess.check_output(["pandoc", "--list-output-formats"]) #TODO if this output fails, then the user does not have pandoc installed. Prompt the user to install pandoc
#options_string = options_string.decode("utf-8")

options = [
    #"asciidoc",
    #"asciidoctor",
    #"beamer",
    #"biblatex",
    #"bibtex",
    #"commonmark",
    #"commonmark_x",
    #"context",
    #"csljson",
    #"docbook",
    #"docbook4",
    #"docbook5",
    "docx",
    #"dokuwiki",
    #"dzslides",
    "epub",
    #"epub2",
    #"epub3",
    #"fb2",
    #"gfm",
    #"haddock",
    "html",
    #"html4",
    #"html5",
    #"icml",
    "ipynb",
    #"jats",
    #"jats_archiving",
    #"jats_articleauthoring",
    #"jats_publishing",
    #"jira",
    "json",
    #"latex",
    #"man",
    "markdown",
    #"markdown_github",
    #"markdown_mmd",
    #"markdown_strict",
    #"markua",
    #"mediawiki",
    #"ms",
    #"muse",
    #"native",
    "odt",
    #"opendocument",
    #"opml",
    #"org",
    "pdf",
    "plain",
    "pptx",
    #"revealjs",
    #"rst",
    #"rtf",
    #"s5",
    #"slideous",
    #"slidy",
    #"tei",
    #"texinfo",
    #"textile",
    #"xwiki",
    #"zimwiki"
]

class filename:
    def __init__(self):
        self.name = ""
    def update_name(self, name):
        self.name = name 

filen = filename()
def pick_file():
    p = fd.askopenfilename()
    print(p)
    filen.update_name(p)
    picked_file.config(text = filen.name)
    picked_file.pack()
    drop.pack()
    convert_button.pack()

root = Tk()
root.geometry("300x200") #TODO change size to fit the full file path so the user doesn't have to resize
root.title("PyPandoc-Gui") #maybe change name
clicked = StringVar()
clicked.set("Pick desired file type") #sets the initial string that shows on the dropdown menu

file_button = Button(root, text="Pick File", command=pick_file).pack()
picked_file = Label(root, text="")

drop = OptionMenu(root, clicked, *options) 

#TODO allow for the user to choose where they want their new file to be located 
#t=Text(root, height=1, width=20)
#t.pack()


dict_endings = { #TODO update this to include all the available file types
    "plain": ".txt",
    "pdf": ".pdf",
    "markdown": ".md",
    "docx": ".docx",
    "odt": ".odt",
    "rtf": ".rtf",
    "pptx": ".pptx",
    "json": ".json",
    "ipynb": ".ipynb",
    "html": ".html",
    "epub": ".epub"
}

success_label = Label(root, text = "")

#may want to abstract this function and remove the gui stuff so the funcion will run with unit tests
def convert(filename, output):
    #run the pandoc command in the terminal 
    output_format = dict_endings.get(output) #TODO put an error exception here
    file = filename.split(".")[0] + output_format #TODO make sure that the correct output format is given (not all file endings are the same as the name in the list)
    print(file)
    command = "pandoc -s " + filen.name + " -o " + file
    os.system(command)
    if os.path.exists(file):
        success_label.config(text="File has been successfully converted")
    else:
        success_label.config(text="Error! File was unable to be successfully converted")
    success_label.pack()
    
def run_convert():
    convert(filen.name, clicked.get())


convert_button = Button(root, text = "Convert", command=run_convert)
root.mainloop()
