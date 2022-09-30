from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import os


# functions
def about():
    about_win = Toplevel()
    about_win.title("About")
    about_win.geometry("700x400")
    about_win.iconbitmap('./images/icon.ico')
    frame = Frame(about_win, width=200, height=200)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("./images/about_transperant.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()
    about_project_label = Label(frame, text="Software name: IP Pinger \n Version: 1.0 \n Usage: IP Pinger is a software for pinging multiple ip addresses from file. \nThe imported file should be in .txt format. In the log tab users can see ping status also can see status of pinging in the result frame. \nFor analysis, users can export the file (D:/readme.txt).")
    about_project_label.pack(pady=20)
    about_me_label = Label(frame, text="Created by Taner Ismail")
    about_me_label.pack(pady=20)
    Button(frame, text='Close', command=about_win.destroy).pack()
    about_win.resizable(False, False)

    about_win.mainloop()


def helper():
    help_win = Toplevel()
    help_win.title("Help")
    help_win.geometry("700x500")
    help_win.iconbitmap('./images/icon.ico')
    frame = Frame(help_win, width=200, height=200)
    frame.pack()

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("./images/about_transperant.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()
    help_text = Label(frame, width=50, text="Main Menu:\n Upload button - open filedialog for upload selected file;\n Upload label: show directory of uploaded file;\n Uploaded text field - show uploaded IP addresses;\n Test IPs button - button for pinging IPs;\n Clear Uploaded IPs button - delete content of uploaded text field; \n Result text field - show result of pinging IPs; \n Export button - export content of result text field; \n Clear result text field - delete content of result text field; \n Logs:\n Logs text field - show ping result for each IP address in format 'ping -n 1 {IP}'; \n About: \n Information about software and useful links.\n Help:\n Information about components and usage.")
    help_text.pack(pady=20)
    Button(frame, text='Close', command=help_win.destroy).pack()
    help_win.resizable(False,False)
    help_win.mainloop()


def show_logs():
    log_win = Toplevel()
    log_win.title("Logs")
    log_win.geometry("400x600")
    log_win.iconbitmap('./images/icon.ico')
    frame = Frame(log_win, width=200, height=200)
    frame.pack()

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("./images/about_transperant.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()
    log_txt = Text(log_win, width=50)
    log_txt.delete("1.0", "end")
    for key in logs.keys():
        log_txt.insert(INSERT, logs[key])
    log_txt.pack(padx=10, pady=10)
    Button(log_win, text='Close', command=log_win.destroy).pack()
    log_win.resizable(False, False)
    log_win.mainloop()


def open_file():
    clear_result_file()
    clear_uploaded_file()
    text_file = filedialog.askopenfilename(initialdir="C:/Desktop", title="Open file", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, 'r')
    rows = text_file.read()
    upload_label.config(text=text_file.name)
    uploaded_text.insert(END, rows)
    text_file.close()
    statusbar.config(text="Waiting...")


def clear_uploaded_file():
    uploaded_text.delete("1.0", "end")


def clear_result_file():
    result_text.delete("1.0", "end")


def test_ips():
    logs.clear()
    line_list = uploaded_text.get('1.0', 'end').split('\n')
    for line in line_list:
        res = os.popen(f"ping -n 1 {line}").read()
        test_if_ip_valid = line.split(".")
        if not (len(test_if_ip_valid) == 4 and all(0 <= int(part) < 256 for part in test_if_ip_valid)):
            result_text.insert(END, line + ' is not a correct IP' + '\n')
        else:
            if "Request timed out." in res:
                result_text.insert(END, line + ' status: No' + '\n')
            else:
                result_text.insert(END, line + ' status: Yes' + '\n')
            logs[f'{line}'] = res

    result_text.delete("end-2l", "end-1l")
    statusbar.config(text="Done!")
    messagebox.showinfo('Test updated IP addresses', 'IP addresses are tested! ')


def export_file():
    with open('D:/readme.txt', 'w') as f:
        line_list = result_text.get('1.0', 'end').split('\n')
        for line in line_list:
            f.write(line + "\n")
    messagebox.showinfo('Export file', 'File is exported in directory D:/readme.txt')
    statusbar.config(text="Ready")


# root
root = Tk()
root.title("IP Pinger")
root.geometry("720x700")
root.iconbitmap('./images/icon.ico')
root.resizable(False, False)
logs = {}

statusbar = Label(root, text="Ready", bd=1, relief=SUNKEN, anchor=W)

statusbar.pack(side=BOTTOM, fill=X)

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
upload_frame = LabelFrame(root, text="Upload .txt file", padx=200, pady=20)
upload_frame.pack(padx=10, pady=10)
upload_button = Button(upload_frame, text="Upload...", command=open_file)
upload_label = Label(upload_frame, text="           Path...")
upload_button.grid(row=0, column=0)
upload_label.grid(row=0, column=2)

# imported file, test them
uploaded_frame = LabelFrame(root, text="Uploaded items", padx=10, pady=10)
scrollbar = Scrollbar(uploaded_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")
uploaded_text = Text(uploaded_frame, width=20)
test_button = Button(uploaded_frame, text="Test IPs", command=test_ips)
clear_uploaded_button = Button(uploaded_frame, text="Clear", command=clear_uploaded_file)
scrollbar.config(command=uploaded_text.yview)
uploaded_text.pack()
test_button.pack(side=LEFT, padx=10, pady=10)
clear_uploaded_button.pack(side=RIGHT, padx=10, pady=10)
uploaded_frame.pack(side=LEFT, padx=100, pady=10)

# result of testing
result_frame = LabelFrame(root, text="Result", padx=10, pady=10)
scrollbar_1 = Scrollbar(result_frame, orient="vertical")
scrollbar_1.pack(side="right", fill="y")
result_text = Text(result_frame, width=25)
scrollbar_1.config(command=result_text.yview)
export_button = Button(result_frame, text="Export file", command=export_file)
clear_result_button = Button(result_frame, text="Clear", command=clear_result_file)
result_text.pack()
export_button.pack(side=LEFT, padx=10, pady=10)
clear_result_button.pack(side=RIGHT, padx=10, pady=10)
result_frame.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
