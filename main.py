"""
by: MOHAMED FARES
This code imports the necessary modules for a Tkinter-based GUI application that uses the moviepy library to perform video editing tasks.

The `tkinter` module provides the core functionality for creating the GUI, including widgets, event handling, and window management.
The `filedialog` module from `tkinter` is used to provide a file selection dialog for the user to choose a video file.
The `moviepy.editor` module provides the core functionality for video editing, including loading, manipulating, and exporting video files.
The `messagebox` module from `tkinter` is used to display informational messages to the user.
"""
from tkinter import *
from tkinter import filedialog
from moviepy.editor import *
from tkinter import messagebox




def convert():
    """
    This function is responsible for converting a video file to an audio file.

    Parameters:
    None

    Returns:
    None

    Raises:
    None

    The function uses the tkinter filedialog module to prompt the user to select a video file.
    Once a video file is selected, it uses the moviepy library to extract the audio from the video.
    The function then prompts the user to save the extracted audio as an MP3 file using the tkinter filedialog module.
    Finally, it displays a success message using the tkinter messagebox module.
    """
    vid = filedialog.askopenfilename(title="Select Video", filetypes=[("Video Files", "*.mp4;*.mkv;*.avi")])
    if vid:
        video = VideoFileClip(vid)
        aud = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
        if aud:
            audio = video.audio
            audio.write_audiofile(aud)
            messagebox.showinfo("Congrats", "Audio file is saved!")


root = Tk()
# give title and Set the size
"""
Sets the geometry of the main window to 300x300 pixels and sets the title to "ProjectMohamedFarez". Adds a label with the text "Convert VIDEO TO AUDIO" and a button with the text "Video to Audio" that calls the `convert` function when clicked.
"""
root.geometry("300x300")
root.title("ProjectMohamedFarez")
Label(root, text=" Convert VIDEO TO AUDIO", bg='Lightblue', font=('Arial 13')).pack()
convert_button = Button(root, text=" Video to Audio", command=convert)
convert_button.pack(pady=20)


root.mainloop()