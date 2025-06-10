from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

fun = Tk()
fun.title("Talha's File Sharer")
fun.geometry("450x560+500+200")
fun.configure(bg = "#f4fdfe")
fun.resizable(False, False)

def SEND():
    window = Toplevel(fun)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg = "#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select Image File', filetype = (('file_type', '*.txt'), ('allfiles', '*.*')))
    
    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print(' waiting for any incoming connections...')
        conn, addr = s.accept()
        file = open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")
    
    #icon
    image_icon1 = PhotoImage(file = "send.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file = "sender.png")
    Label(window, image = Sbackground).place(x = -2, y = 0)

    Mbackground = PhotoImage(file = "id.png")
    Label(window, image = Mbackground, bg = "#f4fdfe").place(x = 100, y = 260)
    
    host = socket.gethostname()
    Label(window, text = f'ID: {host}', bg = 'white', fg = 'black').place(x = 140, y = 290)

    Button(window, text = "+ select file", width = 10, height = 1, font = "Arial 14 bold", bg = "#fff", fg = "#000", command = select_file).place(x = 160, y = 150)
    Button(window, text = "SEND", width = 8, height = 1, font = "Arial 14 bold", bg = "#000", fg = "#fff", command = sender).place(x = 300, y = 150)

    window.mainloop()

def RECEIVE():
    main = Toplevel(fun)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg = "#f4fdfe")
    main.resizable(False, False)

    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        file = open(filename1, 'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print('File has been received successfully')

    #icon
    image_icon1 = PhotoImage(file = "receive.png")
    main.iconphoto(False, image_icon1)
    
    Hbackground = PhotoImage(file = "receiver.png")
    Label(main, image = Hbackground).place(x = -2, y = 0)

    logo = PhotoImage(file = "profile.png")
    Label(main, image = logo, bg = "#f4fdfe").place(x = 10, y = 250)

    Label(main, text = "Receive", font = ("Arial", 20), bg = "#f4fdfe").place(x = 100, y = 280)

    Label(main, text = "Input sender id", font = ("Arial", 10, 'bold'), bg = "#f4fdfe").place(x = 20, y = 340)
    SenderID = Entry(main, width = 25, fg = "black", border = 2, bg = 'white', font = ("Arial", 15))
    SenderID.place(x = 20, y = 370)
    SenderID.focus()

    Label(main, text = "filename for the incoming file", font = ("Arial", 10, 'bold'), bg = "#f4fdfe").place(x = 20, y = 420)
    incoming_file = Entry(main, width = 25, fg = "black", border = 2, bg = 'white', font = ("Arial", 15))
    incoming_file.place(x = 20, y = 450)

    imageicon = PhotoImage(file = "arrow.png")
    rr = Button(main, text = "Receive", compound = LEFT, image = imageicon, width = 130, bg = "#39c790", font = 'Arial 14 bold', command = receiver)
    rr.place(x = 20, y = 500)
    
    main.mainloop()

#icon
image_icon = PhotoImage(file = "icon.png")
fun.iconphoto(False, image_icon)

Label(fun, text = "File Transfer", font = ("Acumin Varbiable Concept", 20, 'bold'), bg = "#f4fdfe").place(x = 20, y = 30)
Frame(fun, width = 400, height = 2, bg = "#f3f5f6").place(x = 25, y = 80)

send_image = PhotoImage(file = "send.png")
send = Button(fun, image = send_image, bg = "#f4fdfe", bd = 0, command = SEND)
send.place(x = 50, y = 100)

receive_image = PhotoImage(file = "receive.png")
receive = Button(fun, image = receive_image, bg = "#f4fdfe", bd = 0, command = RECEIVE)
receive.place(x = 300, y = 100)

#label
Label(fun, text = "Send", font = ("Acumin Variable Concept", 17, 'bold'), bg = "#f4fdfe").place(x = 65, y = 200)
Label(fun, text = "Receive", font = ("Acumin Variable Concept", 17, 'bold'), bg = "#f4fdfe").place(x = 300, y = 200)

background = PhotoImage(file = "background.png")
Label(fun, image = background).place(x = 2, y = 323)

fun.mainloop()