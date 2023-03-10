import tkinter
from tkinter import *
import customtkinter as ct
from playerSelection import PlayerSelection


class CustomsApp(ct.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("League Of Legends Customs Matchmaker")
        self.configure(fg_color="#212121")

        for i in range(14):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)
            # TEST STUFF (for grid visualisation)
            #for j in range(14):
                #ct.CTkButton(master=self, text=f"({i},{j})").grid(row=i, column=j)
        self.player_selection = PlayerSelection(self)

    def start_player_selection(self):
        self.player_selection.start_selection()
    #     self.player_segment_button = ct.CTkSegmentedButton(master=self, values=["Null"],
    #                                                        command=self.player_segment_button_callback,
    #                                                        height=50, font=("Bahnschrift", 20))
    #
    #     self.next_player_button_var = tkinter.StringVar(value="")
    #     self.next_player_button = ct.CTkButton(master=self, textvariable=self.next_player_button_var,
    #                                            command=self.next_player_button_callback,
    #                                            height=30, width=200, font=("Bahnschrift", 15))
    #
    #     self.test_button = ct.CTkButton(master=self, text="beans",
    #                                     command=lambda: self.enable_role_selection_ui(self.selected_players))
    #     self.test_button.grid(column=1, row=3)
    #
    # def player_segment_button_callback(self, value):
    #     if value == self.selected_players[-1]:
    #         self.next_player_button_var.set("Finish")
    #     else:
    #         self.next_player_button_var.set(f"Proceed to {self.selected_players[self.selected_players.index(value)+1]}")
    #
    # def next_player_button_callback(self):
    #     if self.player_segment_button.get() == self.selected_players[-1]:
    #         pass
    #     else:
    #         next_value = self.selected_players[self.selected_players.index(self.player_segment_button.get()) + 1]
    #         self.player_segment_button_callback(next_value)
    #         self.player_segment_button.set(next_value)
    #
    # def enable_role_selection_ui(self, players):
    #     self.player_segment_button.configure(values=players)
    #     self.player_segment_button.set(self.selected_players[0])
    #     self.next_player_button_var.set(f"Proceed to {self.selected_players[1]}")
    #     self.player_segment_button.grid(column=1, row=6, columnspan=5)
    #     self.next_player_button.grid(column=5, row=5)


if __name__ == '__main__':
    app = CustomsApp()
    app.mainloop()
