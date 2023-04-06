import os
import tkinter as tk
from tkinter import filedialog, Frame
from main import sync_folders

source_folder_path = ""
replica_folder_path = ""


def browse_source_folder():
    global source_folder_path
    source_folder_path = filedialog.askdirectory()
    print(f"Source folder: {source_folder_path}")


def browse_replica_folder():
    global replica_folder_path
    replica_folder_path = filedialog.askdirectory()
    print(f"Replica folder: {replica_folder_path}")


def sync_folders_gui():
    global source_folder_path, replica_folder_path
    log_file_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "sync.log")
    if not os.path.exists(log_file_path):
        open(log_file_path, "w").close()
    if source_folder_path and replica_folder_path:
        sync_folders(source_folder_path, replica_folder_path, log_file_path)


root = tk.Tk()
root.title("Sync Folders")
root.geometry("450x250")

frameLeft = Frame(root)
frameLeft.pack(expand=True, fill="x", side="left")

frameRight = Frame(root)
frameRight.pack(expand=True, fill="x", side="left")

btn_source = tk.Button(frameLeft, text="Source Folder",
                       command=browse_source_folder,
                       height=1, width=15)
btn_source.pack(pady=10)

btn_replica = tk.Button(frameLeft, text="Replica Folder",
                        command=browse_replica_folder,
                        height=1, width=15)
btn_replica.pack(pady=10)

btn_sync = tk.Button(
    frameLeft, text="Sync Folders", command=sync_folders_gui, height=1, width=15)
btn_sync.pack(pady=10)

# Configure the global font and colors
font = ("Arial", 10)
bg_color = "#ffffff"
fg_color = "#000000"
button_bg_color = "#0077be"
button_fg_color = "#ffffff"

txt_log = tk.Label(frameRight, font=font, bg=bg_color,
                   fg=fg_color, height=10, width=40, text="The program will sync the selected folders one-way\n and update a log file with any changes made. \n Victor Sav - Test Task")
txt_log.pack(side=tk.RIGHT, padx=10)

root.mainloop()
