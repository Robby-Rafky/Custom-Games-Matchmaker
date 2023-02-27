import tkinter
from tkinter import *
import customtkinter as ct


def segmented_button_callback(value):
    if value == players[-1]:
        test_button_var.set("Finish")
    else:
        test_button_var.set(f"Proceed to {players[players.index(value) + 1]}")


def test_button_callback():
    if segmented_button.get() == players[-1]:
        pass
    # add next stage after all players have been assigned roles.
    else:
        next_value = players[players.index(segmented_button.get()) + 1]
        segmented_button_callback(next_value)
        segmented_button.set(next_value)


ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")
root = ct.CTk()
root.geometry("1280x720")

players = ["player 1", "player 2", "player 3", "player 4", "player 5",
           "player 6", "player 7", "player 8", "player 9", "player 10"]

segmented_button = ct.CTkSegmentedButton(master=root, values=players,
                                         command=segmented_button_callback)
segmented_button.place(relx=0.5, rely=0.8, anchor=CENTER)
segmented_button.set("player 1")

test_button_var = tkinter.StringVar(value="Proceed to player 2")
test_button = ct.CTkButton(master=root, textvariable=test_button_var, command=test_button_callback)
test_button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root.mainloop()
