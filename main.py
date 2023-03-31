import tkinter
from tkinter import *
import customtkinter as ct
from PIL import Image
import os
from playerSelection import PlayerSelection
from roleSelection import RoleSelection


class CustomsApp(ct.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("League Of Legends Customs Matchmaker")
        self.configure(fg_color="#212121")
        ct.set_appearance_mode("dark")

        self.enabled_icon_assets = [x for x in os.listdir("Icon Assets") if "Enabled" in x]
        self.disabled_icon_assets = [x for x in os.listdir("Icon Assets") if "Disabled" in x]
        self.final_icon_assets = [x for x in os.listdir("Icon Assets") if "Final" in x]
        self.enabled_icons = {}
        self.disabled_icons = {}
        self.final_icons = {}

        for enabled, disabled, final in zip(self.enabled_icon_assets,
                                            self.disabled_icon_assets, self.final_icon_assets):
            self.enabled_icons[enabled.split("_", 1)[0]] = ct.CTkImage(dark_image=Image.open(f"Icon Assets/{enabled}"),
                                                                       size=(30, 30))
            self.disabled_icons[disabled.split("_", 1)[0]] = ct.CTkImage(dark_image=Image.open(
                f"Icon Assets/{disabled}"), size=(30, 30))
            self.final_icons[final.split("_", 1)[0]] = ct.CTkImage(dark_image=Image.open(f"Icon Assets/{final}"),
                                                                   size=(30, 30))

        for i in range(14):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)
        self.player_selection = PlayerSelection(self)
        self.role_selection = RoleSelection(self)

        self.start_prog_button = ct.CTkButton(master=self, text="Start", command=lambda: self.start_player_selection(),
                                              height=100, width=400, font=("Bahnschrift", 30))
        self.start_prog_button.grid(row=4, column=4, rowspan=6, columnspan=6)

    def start_player_selection(self):
        self.start_role_selection(['Im a Degen', 'Zaaraus', 'Shwurf', 'Drowningfishes',
                                   'Krasith', 'Lamborjhini', 'Gwft', 'Bearcat', 'Azphra', 'Xen Zenith'])
        # self.player_selection.start_selection()
        self.start_prog_button.grid_forget()

    def start_role_selection(self, players):
        self.role_selection.start_role_selection(players)


if __name__ == '__main__':
    app = CustomsApp()
    app.mainloop()
