from tkinter import filedialog, ttk
from tkinter import messagebox
from tkinter import *
import os


# functions
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


def show_logs():
    log_win = Tk()
    log_win.title("Logs")
    log_win.geometry("700x500")
    log_txt = Text(log_win, width=50)
    for key in logs.keys():
        log_txt.insert(INSERT, logs[key])
    log_txt.pack()
    log_win.mainloop()


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
            result_text.insert(END, line + ' status: No' + '\n')
        else:
            result_text.insert(END, line + ' status: Yes' + '\n')
        logs[f'{line}'] = res

    pb.stop()
    result_text.delete("end-2l", "end-1l")
    messagebox.showinfo('Test updated IP addresses', 'IP addresses are tested! ')


def export_file():
    with open('D:/readme.txt', 'w') as f:
        line_list = result_text.get('1.0', 'end').split('\n')
        for line in line_list:
            f.write(line + "\n")
    messagebox.showinfo('Export file', 'File is exported in directory D:/readme.txt')


# root
root = Tk()
root.title("IP Pinger")
root.geometry("700x500")
root.iconbitmap('./images/icon.ico')
logs = {}

# progress bar
pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
pb.pack(side="bottom")

# menu
my_menu = Menu(root)
root.config(menu=my_menu)
main_menu = Menu(my_menu)
log_menu = Menu(my_menu)
my_menu.add_cascade(label="Main", menu=main_menu)
main_menu.add_command(label="About", command=about)
main_menu.add_command(label="Help", command=helper)
main_menu.add_separator()
main_menu.add_command(label="Exit", command=root.quit)
my_menu.add_cascade(label='Logs', menu=log_menu)
log_menu.add_command(label='Show logs', command=show_logs)

# upload ip from file
upload_frame = LabelFrame(root, text="Upload .csv file", padx=30, pady=20)
upload_frame.pack(padx=10, pady=10)
upload_button = Button(upload_frame, text="Upload...", command=open_file)
upload_label = Label(upload_frame, text="           Path...")
upload_button.grid(row=0, column=0)
upload_label.grid(row=0, column=2)

# imported file, test them
uploaded_frame = LabelFrame(root, text="Uploaded items", padx=30, pady=20)
scrollbar = Scrollbar(uploaded_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")
uploaded_text = Text(uploaded_frame, width=50)
test_button = Button(uploaded_frame, text="Test IPs", command=test_ips)
clear_uploaded_button = Button(uploaded_frame, text="Clear", command=clear_uploaded_file)
scrollbar.config(command=uploaded_text.yview)
uploaded_text.pack()
test_button.pack()
clear_uploaded_button.pack()
uploaded_frame.pack(side=LEFT, padx=100, pady=10)

# result of testing
result_frame = LabelFrame(root, text="Result", padx=30, pady=20)
scrollbar_1 = Scrollbar(result_frame, orient="vertical")
scrollbar_1.pack(side="right", fill="y")
result_text = Text(result_frame, width=50)
scrollbar_1.config(command=result_text.yview)
export_button = Button(result_frame, text="Export file", command=export_file)
clear_result_button = Button(result_frame, text="Clear", command=clear_result_file)
result_text.pack()
export_button.pack()
clear_result_button.pack()
result_frame.pack(side=RIGHT, padx=100, pady=10)

root.mainloop()
