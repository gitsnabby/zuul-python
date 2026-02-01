from tkinter import *
from tkinter import ttk
from game import Game

class Gui:
    def __init__(self, title = "World of Zuul GUI"):
        self.root = Tk()
        self.root.title(title)


        # mainframe = ttk.Frame(self.root, padding=(3, 3, 12, 12))
        # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # # mainframe.config(background="#0a0909", relief="sunken")
        # mainframe.place(width=640, height=480)

        self.display = Text(self.root, width=80, height=20, background="#0a0909", foreground="#00ff2a", wrap="word", font=("Courier", 12, "bold"))
        self.display.grid(column=0, row=0, sticky=(N, W, E), rowspan=10)
        self.display.insert(END, "Welcome to the World of Zuul GUI!\n")
        self.display.config(state=DISABLED)
        self.display_scroll = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.display.yview)
        self.display_scroll.grid(column=1, row=0, sticky=(N, S, E), rowspan=10)
        self.display.config(yscrollcommand=self.display_scroll.set)


        self.input = StringVar()
        self.input_entry = ttk.Entry(self.root, width=80, textvariable=self.input)
        self.input_entry.grid(column=0, row=11, sticky=(W, E))
        self.input_entry.focus()

        self.root.bind('<Visibility>', self.startgame) # call `callback` whenever `root` becomes visible
   
        self.root.bind("<Return>", self.calculate)


        self.feet = StringVar()

        # feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        # feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.meters = StringVar()
        # ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))

        # ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        # ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        # ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)
        # mainframe.columnconfigure(2, weight=1)
        # for child in mainframe.winfo_children(): 
        #     child.grid_configure(padx=5, pady=5)

        self.root.mainloop()

    def startgame(self, event=None):
        # your code here
        game = Game(self)
        self.root.unbind('<Visibility>') # only call `callback` the first time `root` becomes visible



    def print_msg(self, message):
        self.display.config(state=NORMAL)
        self.display.insert(END, message + "\n")
        self.display.config(state=DISABLED)
        self.display.see(END)

    def prep_input(self):
        self.input.set("")
        self.input_entry.focus()

    def start(self):
        pass
    
    def calculate(self, *args):
        pass
        # try:
        #     value = float(self.feet.get())
        #     self.meters.set(str(value * 0.3048))
        # except ValueError:
        #     self.meters.set("Invalid input")