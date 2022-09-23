from tkinter import *
from tkinter import filedialog, ttk
import os

root = Tk()
root.title("IP Pinger")
root.geometry("700x500")


my_menu = Menu(root)
root.config(menu=my_menu)

pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)
pb.pack(side="bottom")


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


def open_file():
    text_file = filedialog.askopenfilename(initialdir="C:/Desktop", title="Open file", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, 'r')
    rows = text_file.read()
    upload_label.config(text=text_file.name)
    uploaded_text.insert(END, rows)
    text_file.close()


def clear_uploaded_file():
    uploaded_text.delete("1.0", "end")


def clear_result_file():
    result_text.delete("1.0", "end")


def test_ips():
    pb.start()
    line_list = uploaded_text.get('1.0', 'end').split('\n')
    for line in line_list:
        res = os.popen(f"ping -n 1 {line}").read()
        if "Request timed out." in res:
            x = line + ' status: No' + '\n'
            result_text.insert(END, x)
        else:
            x = line + ' status: Yes' + '\n'
            result_text.insert(END, x)

    pb.stop()
    result_text.delete("end-2l", "end-1l")



def export_file():
    with open('D:/readme.txt', 'w') as f:
        line_list = result_text.get('1.0', 'end').split('\n')
        for line in line_list:
            f.write(line + "\n")


main_menu = Menu(my_menu)
my_menu.add_cascade(label="Main", menu=main_menu)
main_menu.add_command(label="About", command=about)
main_menu.add_command(label="Help", command=helper)
main_menu.add_separator()
main_menu.add_command(label="Exit", command=root.quit)

upload_frame = LabelFrame(root, text="Upload .csv file", padx=30, pady=20)
upload_frame.pack(padx=10, pady=10)

upload_button = Button(upload_frame, text="Upload...", command=open_file)
upload_label = Label(upload_frame, text="           Path...")
upload_button.grid(row=0, column=0)
upload_label.grid(row=0, column=2)


uploaded_frame = LabelFrame(root, text="Uploaded items", padx=30, pady=20)
myscrollbar = Scrollbar(uploaded_frame, orient="vertical")
myscrollbar.pack(side="right", fill="y")
uploaded_text = Text(uploaded_frame, width=50)
test_button = Button(uploaded_frame, text="Test IPs", command=test_ips)
clear_uploaded_button = Button(uploaded_frame, text="Clear", command=clear_uploaded_file)
myscrollbar.config(command=uploaded_text.yview)
uploaded_text.pack()
test_button.pack()
clear_uploaded_button.pack()
uploaded_frame.pack(side=LEFT, padx=100, pady=10)


result_frame = LabelFrame(root, text="Result", padx=30, pady=20)
myscrollbar_1 = Scrollbar(result_frame, orient="vertical")
myscrollbar_1.pack(side="right", fill="y")
result_text = Text(result_frame, width=50)
myscrollbar_1.config(command=result_text.yview)
export_button = Button(result_frame, text="Export file")
clear_result_button = Button(result_frame, text="Clear", command=clear_result_file)
result_text.pack()
export_button.pack()
clear_result_button.pack()
result_frame.pack(side=RIGHT, padx=100, pady=10)

root.mainloop()
