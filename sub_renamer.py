import glob
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os

def file_open():
    from tkinter import filedialog
    path_name = filedialog.askdirectory()
    path_entry.delete(0,END)
    path_entry.insert(0,path_name)

def rename_files():
    path_name=path_entry.get()
    try:
        os.chdir(path_name)
    except:
        messagebox.showerror("Error", "Path error")
    vid_ext=vid_combo.get()
    sub_ext=sub_combo.get()
    sub_files = glob.glob("*."+sub_ext)
    video_files = glob.glob("*."+vid_ext)

    if(rename_choice.get()==0):
        if (len(sub_files) != len(video_files)) or (len(sub_files)==0):
            messagebox.showerror("Error", "Some files are missing or you are in the wrong directory")
            return
        else:
            for i in range(len(video_files)):
                os.rename(video_files[i], sub_files[i][:-(len(sub_ext)+1)] + "." + vid_ext)

    else:
        if (len(sub_files) != len(video_files)) or (len(sub_files)==0):
            messagebox.showerror("Error", "Some files are missing or you are in the wrong directory")
            return
        else:
            for i in range(len(video_files)):
                os.rename(sub_files[i], video_files[i][:-(len(vid_ext)+1)] + "." + sub_ext)

    rename_button.configure(text="Successful", fg="green")

window=tkinter.Tk()
window.title("Sub renamer")

rename_choice=tkinter.IntVar()
path_label=tkinter.Label(window, text="Select directory:",anchor="w", height=2, width=25, justify=LEFT)
path_label.grid(column=0,row=0)

path_entry=tkinter.Entry(window, width=65)
path_entry.grid(column=1,row=0)

path_button=tkinter.Button(window, text="Path", command= file_open)
path_button.grid(column=2,row=0)

vid_label=tkinter.Label(window, text="Select Video file extension: ", anchor="w", width=25, justify=LEFT)
vid_label.grid(column=0,row=2)
vid_combo=Combobox(window, width=25, justify=LEFT)
vid_combo['values']=("mkv","mp4","avi")
vid_combo.grid(column=0,row=3)


sub_label=tkinter.Label(window, text="Select Subtitle file extension: ",anchor="w", width=25, justify=LEFT)
sub_label.grid(column=1,row=2)
sub_combo=Combobox(window, width=25, justify=LEFT)
sub_combo['values']=("srt","ass")
sub_combo.grid(column=1,row=3)

rename_vid=tkinter.Radiobutton(window,text="Rename Video", anchor="w", width=22, justify=LEFT, variable=rename_choice, value=0)
rename_sub=tkinter.Radiobutton(window,text="Rename Subtitles", anchor="w", width=22, justify=LEFT, variable=rename_choice, value=1)
rename_vid.grid(column=0,row=5)
rename_sub.grid(column=1,row=5)

rename_button=tkinter.Button(window,text="Rename", command=rename_files)
rename_button.grid(column=1,row=6)

window.geometry('720x300')
window.mainloop()

