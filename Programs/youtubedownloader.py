import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    save_path = filedialog.askdirectory()
    if not url or not save_path:
        messagebox.showerror("Error", "Please provide both URL and save path.")
        return

    try:
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        ys.download(save_path)
        messagebox.showinfo("Success", f"Downloaded '{yt.title}' successfully!")
    except Exception as e:
        if "regex_search" in str(e):
            messagebox.showerror("Error", "Invalid YouTube URL.")
        else:
            messagebox.showerror("Error", f"Failed to download video: {e}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL input
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=1, columnspan=2, pady=10)

# Run the application
root.mainloop()
