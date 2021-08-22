from tkinter import *
from pytube import YouTube

# creating tkinter window
root = Tk()
# creating fixed geometry of the
# tkinter window with dimensions 500x300
root.geometry('500x300')
# Restricting root window to change
# it's size according to user's need
root.resizable(0, 0)
root.title("Ido Pinto - Youtube Downloader")
# Label() widget use to display text that users can't able to modify.
# root is the name of the window
# text which we display the title of the label
# font in which our text is written
# pack organized widget in block
Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

# link is a string type variable that stores the youtube video link that the user enters
link = StringVar()
Label(root, text='Paste Link Here', font='arial 15 bold').place(x=160, y=60)
# Entry() widget is used when we want to create an input text field
# width sets the width of entry widget
# textvariable used to retrieve the value of current text variable to the entry widget
# place() use to place the widget at a specific position
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


# create Function to start downloading
def Downloader():
    """
    this function gets youtube url from user and download it
    :return:
    """
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    song_name = video.title
    Label(root, text=' DOWNLOADED', font='arial 15').place(x=180, y=210)
    Label(root, text= song_name , font='arial 12').place(x=120, y=260)

# Button widget used to display button on the window
# text which we display on the label
# font in which the text is written
# bg sets the background color
# command is  used to call the function ** without ()** e.g Downloader and not Downloader()

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180,
                                                                                                              y=150)
# method that executes when we want to run the program
root.mainloop()
