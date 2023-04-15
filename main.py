import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convertToKilo():
    input = entry_input.get()
    output_value.set(input*1.61)
# main widget
#window = tk.Tk()
window = ttk.Window(themename="darkly")

# set title
window.title("Miles to kilometers")

# set size
# set custom window width and height
screen_width = 600
screen_height = 250

# calculate x and y coordinates for the top-left corner of the window
x = int((screen_width - window.winfo_reqwidth()) / 2)
y = int((screen_height - window.winfo_reqheight()) / 2)

# set the window size and position
window.geometry(f"{screen_width}x{screen_height}+{x}+{y}")


# create a label widget with text
##################################################################
##################################################################
label_frame = tk.Frame(window,padx=50, 
                pady=20)
label = tk.Label(label_frame, 
                text="Miles to kilometers", 
                font=("Arial", 20),
                bg="blue", fg="white", 
                padx=20, 
                pady=5, 
                borderwidth=2, 
                relief="groove")

# pack the label widget to display it in the window
label_frame.pack()
label.pack()
##################################################################
##################################################################
# create a frame widget to hold the input field and button
input_frame = tk.Frame(window, bg="#fff")

# create an input field widget and add it to the frame
entry_input = tk.IntVar()
input_field = tk.Entry( input_frame, 
                        width       = 30, 
                        font        = ("Arial", 12),
                        bg          = "#eee", fg="#333",
                        borderwidth = 2, 
                        relief      = "groove",
                        textvariable= entry_input)
input_field.pack(side=tk.LEFT, padx=5)

# create a button widget and add it to the frame
button = tk.Button(input_frame, text="Convert", font=("Arial", 12), bg="#007bff", fg="#fff", activebackground="#0062cc", activeforeground="#fff", borderwidth=2, relief="groove", command=convertToKilo)
button.pack(side=tk.LEFT, padx=5)

input_frame.pack()
##################################################################
##################################################################

# create a label widget with text
label_output_frame = tk.Frame(window,padx=50, 
                pady=20)
output_value = tk.StringVar()
label_output = tk.Label(label_output_frame, 
                text="output", 
                font=("Arial", 20),
                bg="blue", fg="white", 
                padx=20, 
                pady=5, 
                borderwidth=0, 
                relief="groove",
                textvariable=output_value)

# pack the label widget to display it in the window
label_output_frame.pack()
label_output.pack()
##################################################################
##################################################################
#run
window.mainloop()