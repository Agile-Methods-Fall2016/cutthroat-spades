from CutthroatGame import main_game
from Tkinter import Tk, Label, Button, Entry, Message


class SpadesMenu:
    def __init__(self, master):
        self.master = master
        master.title("Cutthroat Killer Spades Menu")
        current_row = 0
        column_span = 2

        self.labelTitle = Label(master, text="Cutthroat Killer Spades")
        self.labelTitle.grid(row=current_row, columnspan=column_span)
        current_row += 1

        self.labelServerIP = Label(master, text="IP of Server:")
        self.labelServerIP.grid(row=current_row, column=0)

        self.entryServerIP = Entry(master)
        self.entryServerIP.grid(row=current_row, column=1)
        current_row += 1

        self.connect_button = Button(master, text="Connect", command=self.connect_to_server)
        self.connect_button.grid(row=current_row, columnspan=column_span)
        current_row += 1

        self.connection_message_text = "Connect to server to play.\n"
        self.connection_message = Message(master, text=self.connection_message_text, width=1000)
        self.connection_message.grid(row=current_row, columnspan=column_span)
        current_row += 1

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=current_row, columnspan=column_span)

        self.server_ip = ""


    def connect_to_server(self):
        self.server_ip = self.entryServerIP.get()
        self.connection_message_text += "Connecting to server at " + self.server_ip + "\n"
        self.connection_message.configure(text=self.connection_message_text)



def menu():
    root = Tk()
    my_gui = SpadesMenu(root)
    root.mainloop()

if __name__ == '__main__':
    menu()

