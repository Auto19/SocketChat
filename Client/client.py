from Tkinter import *
from socket import *
import thread
import socket




print("before you get to chat please give us your username, please do not be vulgar")

h = raw_input(":")

host = raw_input("What is the hosts ip address: ")

e = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (host, PORT)

counter = 0
Insertline = 1.0

tcpCliSock = socket.socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.socket()

    def callback(self, event):
        message = self.entry_field.get()
        self.entry_field.delete("0", END)
        tcpCliSock.send(h + "(" + str(e) + ")" + ":" + message)

    def create_widgets(self):
        
        self.messaging_field = Text(self, width = 70, height = 15, wrap = WORD)
        self.messaging_field.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.entry_field = Entry(self, width = 80)
        
        self.entry_field.grid(row = 1, column = 0, sticky = W)
        self.entry_field.bind('<Return>', self.callback)
        
    def add(self, data):
        global counter
        self.messaging_field.tag_configure('highlightline1', background='blue', font='helvetica 10', relief='raised')
        self.messaging_field.tag_configure('highlightline2', background='red', font='helvetica 10', relief='raised')
        self.messaging_field.tag_configure('highlightline3', background='green', font='helvetica 10', relief='raised')
        self.messaging_field.tag_configure('highlightline4', background='pink', font='helvetica 10', relief='raised')
        self.messaging_field.tag_configure('highlightline5', background='orange', font='helvetica 10', relief='raised')
        
        if ".." in data:
            self.messaging_field.insert(END, data, ('highlightline5'))
        elif "/\\" in data:
            self.messaging_field.insert(END, data, ('highlightline4'))
        elif "#" in data:
            self.messaging_field.insert(END, data, ('highlightline3'))
        elif "IT" in data:
            self.messaging_field.insert(END, data, ('highlightline1'))
        elif "!?!" in data:
            self.messaging_field.insert(END, data, ('highlightline2'))
        else:
            self.messaging_field.insert(END, data)
        counter = counter + 1
        
        if(counter == 16):
            self.messaging_field.delete("1.0", "2.0")
            counter = counter - 1            

    def socket(self):
        def loop0():
            while 1:
                data = tcpCliSock.recv(BUFSIZE)
                if data: self.add(data)

        thread.start_new_thread(loop0, ())



root = Tk()
root.title("Chat client")
root.geometry("550x260")

app = Application(root)

root.mainloop()
