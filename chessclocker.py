from tkinter import *
import math, time

class Clock:
    def __init__(self):
        self.bonus_time = 0
        self.is_left = 1
        self.is_right = 0
        self.is_going = 0
        self.fenster = Tk()
        self.fenster.title("Best Chess Timer")
        self.frame = Frame(self.fenster, relief=GROOVE, bd=4)
        self.entry_frame = Frame(self.fenster)

        self.right_time, self.left_time = 0, 0

        self.c1 = Label(self.frame, padx=10, pady=5,
              font=("Arial", 60), relief=RIDGE, bd=6, fg="green")
        self.leftconfig()


        self.c2 = Label(self.frame, padx=10, pady=5,
              font=("Arial", 60), relief=RIDGE, bd=6)
        self.rightconfig()


        self.set_button_left = Button(self.fenster, text="set",
                                      command=self.set_left, font=("Arial", 12))


        self.set_button_right = Button(self.fenster, text="set",
                                      command=self.set_right, font=("Arial", 12))


        self.start_button = Button(self.fenster, text="start", activebackground='green',
                             relief=RAISED, bd=4, command=self.start, font=("Arial", 15))

        self.pause_button = Button(self.fenster, text="pause", activebackground='red',
                             relief=RAISED, bd=4, command=self.pause, font=("Arial", 15))


        self.entry_left = Entry(self.entry_frame, width=10)
        self.entry_right = Entry(self.entry_frame, width=10, text="right")
        self.left_min = Label(self.entry_frame, text="min.")
        self.right_min = Label(self.entry_frame, text="min.")
        self.command_frame = Frame(self.fenster, padx=6, pady=2)
        self.sign_label = Label(self.command_frame, text="Shift_Left <switch> Shift_Right",
                                font=("Times", 15, "italic"))
        self.mode_frame = Frame(self.fenster, padx=6, pady=2)
        self.mode_entry = Entry(self.mode_frame, width=6, font=("Arial", 14))
        self.mode_entry.focus_set()
        self.mode_button = Button(self.mode_frame, text="config",
                                  command=self.time_config)
        self.layout()
        self.fenster.bind("<KeyPress-Shift_L>", self.change_to_right)
        self.fenster.bind("<KeyPress-Shift_R>", self.change_to_left)
        self.fenster.bind("<space>", self.space_pressed)
        self.fenster.mainloop()

    def layout(self):
        self.frame.pack(padx=6, pady=2)
        self.entry_frame.pack(padx=6, pady=2)
        self.c1.pack(side=LEFT)
        self.c2.pack(side=RIGHT)
        self.set_button_left.pack(side=LEFT, padx=20)
        self.set_button_right.pack(side=RIGHT, padx=20)
        Label(self.entry_frame, text=" ", padx=100).grid(column=2, row=2)
        self.start_button.pack(anchor=CENTER)
        self.sign_label.pack()
        self.command_frame.pack()
        self.mode_button.pack(side=RIGHT)
        self.mode_entry.pack(side=RIGHT)
        Label(self.mode_frame, text="mode: ").pack(side=LEFT)
        self.mode_frame.pack(side=BOTTOM)

    def set_left(self):
        self.entry_left.focus_set()
        self.left_min.grid(column=1, row=2)
        self.set_button_left.config(text="ok", command=self.zuruecksetzen_left)
        self.entry_left.grid(column=0, row=2)
        self.pause()

    def set_right(self):
        self.entry_right.focus_set()
        self.right_min = Label(self.entry_frame, text="min.")
        self.right_min.grid(column=4, row=2)
        self.set_button_right.config(text="ok", command=self.zuruecksetzen_right)
        self.entry_right.grid(column=3, row=2)
        self.is_going = 0
        self.pause()

    def zuruecksetzen_left(self):
        if self.entry_left.get() and not self.entry_left.get().isalpha():
            self.entry_left.grid_forget()
            self.left_min.grid_forget()
            self.left_time = int(float(self.entry_left.get()) * 60)
            self.leftconfig()
            self.set_button_left.config(text="set", command=self.set_left)

    def leftconfig(self):
        self.c1.config(text=str(int(self.left_time / 60)) + ':' + \
                            str(self.left_time % 60))
        if self.left_time % 60 < 10:
            self.c1.config(text=str(int(self.left_time / 60)) + ':' + \
                                '0' + str(int(self.left_time % 60)))
            if self.left_time / 60 < 10:
                self.c1.config(text='0' + str(int(self.left_time / 60)) + ':' + \
                                    '0' + str(int(self.left_time % 60)))
        else:
            if self.left_time / 60 < 10:
                self.c1.config(text='0' + str(int(self.left_time / 60)) + ':' + \
                                    str(int(self.left_time % 60)))

    def zuruecksetzen_right(self):
        if self.entry_right.get() and not self.entry_right.get().isalpha():
            self.entry_right.grid_forget()
            self.right_min.grid_forget()
            self.right_time = float(self.entry_right.get()) * 60
            self.rightconfig()
            self.set_button_right.config(text="set", command=self.set_right)

    def rightconfig(self):
        self.c2.config(text=str(int(self.right_time / 60)) + ':' + \
                            str(self.right_time % 60))
        if self.right_time % 60 < 10:
            self.c2.config(text=str(int(self.right_time / 60)) + ':' + \
                                '0' + str(int(self.right_time % 60)))
            if self.right_time / 60 < 10:
                self.c2.config(text='0' + str(int(self.right_time / 60)) + ':' + \
                                    '0' + str(int(self.right_time % 60)))
        else:
            if self.right_time / 60 < 10:
                self.c2.config(text='0' + str(int(self.right_time / 60)) + ':' + \
                                    str(int(self.right_time % 60)))

    def time_config(self):
        bonus = self.mode_entry.get()
        try:
            l = bonus.split("+")
            self.bonus_time = float(l[1])
            self.right_time, self.left_time = int(float(l[0]) * 60), int(float(l[0]) * 60)
        except:
            self.right_time, self.left_time = int(float(bonus) * 60), int(float(bonus) * 60)
        self.rightconfig()
        self.leftconfig()


    def run(self):
        if self.is_going:
            if self.is_left and self.left_time > 0:
                self.left_time -= 1
                self.leftconfig()
            elif self.is_right and self.right_time > 0:
                self.right_time -= 1
                self.rightconfig()
            if self.left_time <= 0:
                self.c1.config(fg="red")
                self.is_going = 0
            elif self.right_time <=0:
                self.c2.config(fg="red")
                self.is_going = 0

            self.fenster.after(1000, self.run)

    def start(self):
        self.is_going = 1
        self.fenster.focus_set()
        if self.is_going:
            self.run()
            self.start_button.pack_forget()
            self.pause_button.pack(anchor=CENTER)
            return

    def pause(self):
        if self.is_going:
            self.pause_button.pack_forget()
            self.start_button.config(text="continue")
            self.start_button.pack(anchor=CENTER)
            self.is_going = 0

    def change_to_left(self, event=None):
        if self.is_going == 1 and self.is_right:
            self.right_time += self.bonus_time
            self.rightconfig()
        self.is_left = 1
        self.is_right = 0
        self.sign_label.config(text="Left's turn")
        self.c1.config(fg="green")
        self.c2.config(fg="black")

    def change_to_right(self, event=None):
        if self.is_going == 1 and self.is_left:
            self.left_time += self.bonus_time
            self.leftconfig()
        self.is_right = 1
        self.is_left = 0
        self.sign_label.config(text="Right's turn")
        self.c2.config(fg="green")
        self.c1.config(fg="black")


    def space_pressed(self, event=None):
        if self.is_going:
            self.pause()
        else:
            self.start()


C = Clock()
