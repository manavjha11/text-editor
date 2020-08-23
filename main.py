import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("mainpad text editor")

########################### main menu ############################

main_menu = tk.Menu()
########################## file ##########################
file = tk.Menu(main_menu, tearoff=False)

new_icon = tk.PhotoImage(file="manav//new.png")
open_icon = tk.PhotoImage(file="manav//open.png")
save_icon = tk.PhotoImage(file="manav//save.png")
save_as_icon = tk.PhotoImage(file="manav//saveas.png")
exit_icon = tk.PhotoImage(file="manav//exit.png")

############################# file end #####################

############################# edit ##########################
edit = tk.Menu(main_menu, tearoff=False)

copy_icon = tk.PhotoImage(file="manav//copy.png")
cut_icon = tk.PhotoImage(file="manav//cut.png")
paste_icon = tk.PhotoImage(file="manav//paste.png")
clear_all_as_icon = tk.PhotoImage(file="manav//clearall.png")
find_icon = tk.PhotoImage(file="manav//find.png")

############################ edit end ##################### 

############################ view ############################
view = tk.Menu(main_menu, tearoff=False)
tool_bar_icon = tk.PhotoImage(file="manav//toolbar.png")
status_bar_icon = tk.PhotoImage(file="manav//statusbar.png")

######################### view end ########################


######################## cascade ###########################

main_menu.add_cascade(label="file", menu=file)
main_menu.add_cascade(label="edit", menu=edit)
main_menu.add_cascade(label="view", menu=view)

###########################  end  ###############################

######################### tool bar ############################
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

font_tuple = tk.font.families()
fontfamily = tk.StringVar()
fontbox = ttk.Combobox(tool_bar, width=30, textvariable=fontfamily, state='readonly')
fontbox['values'] = font_tuple
fontbox.current(font_tuple.index('Arial'))
fontbox.grid(row=0, column=0, padx=5)

font_var = tk.StringVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=font_var, state='readonly')
font_size['values'] = tuple(range(0, 81, 2))
font_size.current(6)
font_size.grid(row=0, column=1, padx=5)

underline_icon = tk.PhotoImage(file='manav//underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=3, padx=5)

bold_icon = tk.PhotoImage(file='manav//bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

italic_icon = tk.PhotoImage(file='manav//italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=4, padx=5)

fontcolor_icon = tk.PhotoImage(file='manav//font_color.png')
fontcolor_btn = ttk.Button(tool_bar, image=fontcolor_icon)
fontcolor_btn.grid(row=0, column=5, padx=5)

leftalign_icon = tk.PhotoImage(file='manav//leftalign.png')
leftalign_btn = ttk.Button(tool_bar, image=leftalign_icon)
leftalign_btn.grid(row=0, column=6, padx=5)

centeralign_icon = tk.PhotoImage(file='manav//centeralign.png')
centeralign_btn = ttk.Button(tool_bar, image=centeralign_icon)
centeralign_btn.grid(row=0, column=7, padx=5)

rightalign_icon = tk.PhotoImage(file='manav//rightalign.png')
rightalign_btn = ttk.Button(tool_bar, image=rightalign_icon)
rightalign_btn.grid(row=0, column=8, padx=5)

##############################tool bar end ##################

############################## text editor #################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)
scroolbar = tk.Scrollbar(main_application)
scroolbar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.focus_set()
text_editor.pack(fill=tk.BOTH, expand=True)
scroolbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroolbar.set)

## font size and families 
currentfontfamily = 'Arial'
currentfontsize = 12

def changefont(main_application):
    global currentfontfamily
    currentfontfamily = fontfamily.get()
    text_editor.configure(font=(currentfontfamily, currentfontsize))

def changefontsize(main_application):
    global currentfontsize
    currentfontsize = font_var.get()
    text_editor.configure(font=(currentfontfamily, currentfontsize))

fontbox.bind('<<ComboboxSelected>>', changefont)
font_size.bind('<<ComboboxSelected>>', changefontsize)

##### bold ########
def changebold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(currentfontfamily, currentfontsize, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(currentfontfamily, currentfontsize, 'normal'))

bold_btn.configure(command=changebold)

########## italic #####
def changeitalic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(currentfontfamily, currentfontsize, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(currentfontfamily, currentfontsize, 'normal'))

italic_btn.configure(command=changeitalic)

###### underline ######
def changeunderline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(currentfontfamily, currentfontsize, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(currentfontfamily, currentfontsize, 'normal'))

underline_btn.configure(command=changeunderline)

###### change font #######
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

fontcolor_btn.configure(command=change_font_color)   

####### align left ######
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('lift', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

leftalign_btn.configure(command=align_left)  

####### align right ######
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

rightalign_btn.configure(command=align_right)    

####### align center ######
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

centeralign_btn.configure(command=align_center)  

text_changed = True
def changed(event=None):
    if text_editor.edit_modified():
        words = len(text_editor.get(1.0, 'end-1c').split())
        chractors = len(text_editor.get(1.0, 'end-1c'))
        text_changed = False
        statusbar.configure(text=f"charactors : {chractors} ,  words :{words}")
        text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)


text_editor.configure(font=('Arial', 12))

############################## text editor end ############

########################### status bar ######################

statusbar = ttk.Label(main_application, text='status bar')
statusbar.pack(side=tk.BOTTOM)

######################## status bar end ######################

###################### main menu functionalty #####################

url = ''
#### new ####
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

#### open #####
def openfile(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='select file', filetypes=(('text file', '*.txt'), ('all files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
         return
    main_application.title(os.path.basename(url)) 

##### save file ####
def save_file(event=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('text file', '*.txt'), ('all files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return  

def save_as(event=None):
    try:
        content = text_editor.get(1.0, tk.END) 
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('text file', '*.txt'), ('all files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('warning', 'do you want to save this file ?')
            if mbox :
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('text file', '*.txt'), ('all files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()

            else:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return  

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')


    def replace():
        word = find_input.get()
        replace = find_replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('find')
    find_dialogue.resizable(0, 0)                    

    ########## frame ####
    find_frame = ttk.LabelFrame(find_dialogue, text='find/replace')
    find_frame.pack(pady=20)

    ###### label
    text_find_label = ttk.Label(find_frame, text='find : ')
    text_replace_label = ttk.Label(find_frame, text='replace : ')

    ##### entry
    find_input = ttk.Entry(find_frame, width=30)
    find_replace_input = ttk.Entry(find_frame, width=30)

    ###### button
    find_button = ttk.Button(find_frame, text='find', command=find)
    replace_button = ttk.Button(find_frame, text='replace', command=replace)

    ###### grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    find_input.grid(row=0, column=1, padx=4, pady=4)
    find_replace_input.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

###### view ######
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        statusbar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)    
        statusbar.pack(fill=tk.BOTTOM)    
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        statusbar.pack_forget()
        show_statusbar = False
    else:
        statusbar.pack(side=tk.BOTTOM)
        show_statusbar = True


file.add_command(label="new", image=new_icon, compound=tk.LEFT, accelerator="ctrl+N", command=new_file)
file.add_command(label="open", image=open_icon, compound=tk.LEFT, accelerator="ctrl+O", command=openfile)
file.add_command(label="save", image=save_icon, compound=tk.LEFT, accelerator="ctrl+S", command=save_file)
file.add_command(label="save as", image=save_as_icon, compound=tk.LEFT, accelerator="ctrl+A", command=save_as)
file.add_command(label="exit", image=exit_icon, compound=tk.LEFT, accelerator="ctrl+Q", command=exit_func)
edit.add_command(label="copy", image=copy_icon, compound=tk.LEFT, accelerator="ctrl+C", command=lambda:text_editor.event_generate('<control c>'))
edit.add_command(label="cut", image=cut_icon, compound=tk.LEFT, accelerator="ctrl+V", command=lambda:text_editor.event_generate('<control x>'))
edit.add_command(label="paste", image=paste_icon, compound=tk.LEFT, accelerator="ctrl+X", command=lambda:text_editor.event_generate('<control v>'))
edit.add_command(label="clearall", image=clear_all_as_icon, compound=tk.LEFT, accelerator="ctrl+Alt+X", command=lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label="find", image=find_icon, compound=tk.LEFT, accelerator="ctrl+F", command=find_func)

view.add_checkbutton(label="tool bar",onvalue=True, offvalue=0,variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="status bar",onvalue=1, offvalue=False,variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)



######################### main menu functionalty end #################

main_application.config(menu=main_menu)

##### bind keys ######
main_application.bind('<Control-n>', new_file)
main_application.bind('<Control-o>', openfile)
main_application.bind('<Control-s>', save_file)
main_application.bind('<Control-a>', save_as)
main_application.bind('<Control-q>', exit_func)
main_application.bind('<Control-f>', find_func)

main_application.mainloop()





