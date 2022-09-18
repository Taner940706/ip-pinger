from tkinter import *

root = Tk()
root.title("IP Pinger")
root.geometry("700x500")


my_menu = Menu(root)
root.config(menu=my_menu)


def about():
    about_win = Tk()
    about_win.title("About")
    about_win.geometry("700x500")
    about_win.mainloop()


def helper():
    help_win = Tk()
    help_win.title("Help")
    help_win.geometry("700x500")
    help_win.mainloop()


main_menu = Menu(my_menu)
my_menu.add_cascade(label="Main", menu=main_menu)
main_menu.add_command(label="About", command=about)
main_menu.add_command(label="Help", command=helper)
main_menu.add_separator()
main_menu.add_command(label="Exit", command=root.quit)

upload_frame = LabelFrame(root, text="Upload .csv file", padx=30, pady=20)
upload_frame.pack(padx=10, pady=10)

upload_button = Button(upload_frame, text="Upload...")
upload_label = Label(upload_frame, text="           Path...")
import_button = Button(upload_frame, text="Import")
clear_button = Button(upload_frame, text="Clear")
label_sep = Label(upload_frame, text="            ")
upload_button.grid(row=0, column=0)
upload_label.grid(row=0, column=2)
label_sep.grid(row=1, column=0)
label_sep.grid(row=2, column=0)
label_sep.grid(row=3, column=0)
label_sep.grid(row=4, column=0)
import_button.grid(row=5, column=0)
clear_button.grid(row=5, column=1)

uploaded_frame = LabelFrame(root, text="Uploaded items", padx=30, pady=20)
uploaded_frame.pack(padx=10, pady=10)
uploaded_label = Label(uploaded_frame, text="IPs...", width=50)
test_button = Button(uploaded_frame, text="Test IPs")
clear_uploaded_button = Button(uploaded_frame, text="Clear")
uploaded_label.grid(row=0, column=0)
test_button.grid(row=1, column=0)
clear_uploaded_button.grid(row=1, column=1)

result_frame = LabelFrame(root, text="Result", padx=30, pady=20)
result_frame.pack(padx=10, pady=10)
result_label = Label(result_frame, text="IPs...", width=50)
export_button = Button(result_frame, text="Export file")
clear_result_button = Button(result_frame, text="Clear")
result_label.grid(row=0, column=0)
export_button.grid(row=1, column=0)
clear_result_button.grid(row=1, column=1)
root.mainloop()
