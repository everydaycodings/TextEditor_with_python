import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox

class Menubar:

    def __init__(self, parent):
        font_specs = ("Sans Italic", 12)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open File",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Save",
                                  command=parent.save)
        file_dropdown.add_command(label="Save As",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",
                                  command=parent.c_exit)
        menubar.add_cascade(label="File", menu=file_dropdown)

        file_dropdown_2 = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown_2.add_command(label="Undo", command=parent.textarea.edit_undo)
        file_dropdown_2.add_command(label="Redo", command=parent.textarea.edit_redo)
        file_dropdown_2.add_separator()
        file_dropdown_2.add_command(label="Cut", command= parent.cut_text)
        file_dropdown_2.add_command(label="Copy", command= parent.copy_text)
        file_dropdown_2.add_command(label="Paste", command= parent.paste_text)
        file_dropdown_2.add_command(label="Delete")
        file_dropdown_2.add_separator()
        file_dropdown_2.add_command(label="Sellect All")
        menubar.add_cascade(label="Edit", menu=file_dropdown_2)

        file_dropdown_3 = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown_3.add_command(label="About", command=parent.info)
        menubar.add_cascade(label="Help", menu=file_dropdown_3)


class PyText:

    def __init__(self, master):
        master.title("Untitled - PyText")
        master.geometry("600x400")
        font_specs = ("Source Code Pro", 12)

        self.master = master
        self.filename = None

        self.textarea = tk.Text(self.master, font=font_specs, undo= True)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.menubar = Menubar(self)

    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - PyText")
        else:
            self.master.title("Untitled - PyText")

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)
    
    def save(self):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)

    def c_exit(self):
        self.answer = tk.messagebox.askyesno("QUIT","Do You Really Want To Quit?")
        if (self.answer):
            quit()

    def info(self):
        self.introduction = tk.messagebox.showinfo("About", "This Is A TextEditor Made By Kumar Saksham"
                                                            " For Experimental Purpose")

    def cut_text(self):
        self.copy_text()
        self.textarea.delete("sel.first", "sel.last")

    def copy_text(self):
        self.textarea.clipboard_clear()
        self.textarea.clipboard_append(self.textarea.selection_get())

    def paste_text(self):
        self.textarea.insert(tk.INSERT, self.textarea.clipboard_get())


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
