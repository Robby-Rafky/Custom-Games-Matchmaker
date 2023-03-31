import tkinter
import customtkinter as ct
import json


class PlayerSelection:
    def __init__(self, app):
        self.parent_app = app

        self.selected_players = []
        self.query_players = []

        self.player_list = []
        self.player_data = None

        self.player_query_buttons = []
        self.query_vars = []

        self.selected_vars = []
        self.selected_buttons = []

        self.player_entry_box = ct.CTkEntry(master=self.parent_app, placeholder_text="Search Players",
                                            width=450, height=45, border_width=2, corner_radius=10,
                                            font=("Bahnschrift", 25))
        self.player_entry_box.bind("<KeyRelease>", lambda event: self.search_player(self.player_entry_box.get()))

        self.selected_players_text_box = ct.CTkLabel(master=self.parent_app, text="Selected Players",
                                                     width=400, height=45, font=("Bahnschrift", 22))
        self.end_selection_button = ct.CTkButton(master=self.parent_app, text="Select more players",
                                                 width=400, height=45, font=("Bahnschrift", 22),
                                                 fg_color="#212121", hover_color="#242424", state="disabled",
                                                 command=lambda: self.end_selection())

        for i in range(8):
            self.query_vars.append(tkinter.StringVar(value=" "))
            self.player_query_buttons.append(ct.CTkButton(master=self.parent_app, height=45, width=450,
                                                          textvariable=self.query_vars[i], font=("Bahnschrift", 17),
                                                          fg_color="#212121", hover_color="#242424",
                                                          command=lambda x=i: self.select_player(self.query_vars[x])))
        for i in range(10):
            self.selected_vars.append(tkinter.StringVar(value=" "))
            self.selected_buttons.append(ct.CTkButton(master=self.parent_app, height=45, width=400,
                                                      textvariable=self.selected_vars[i], font=("Bahnschrift", 15),
                                                      fg_color="#212121", hover_color="#242424",
                                                      command=lambda x=i: self.remove_player(self.selected_vars[x])))

    def start_selection(self):
        for i, item in enumerate(self.player_query_buttons):
            item.grid(column=1, row=2 + i, columnspan=6, rowspan=1)
        for i, item in enumerate(self.selected_buttons):
            item.grid(column=8, row=2 + i, columnspan=6, rowspan=1)
        self.selected_players_text_box.grid(column=8, row=1, columnspan=6)
        self.player_entry_box.grid(column=1, row=1, columnspan=6, rowspan=1)
        self.end_selection_button.grid(row=12, column=8, columnspan=6, rowspan=1)

        self.load_players()
        self.search_player("")

    def end_selection(self):
        for i, item in enumerate(self.player_query_buttons):
            item.grid_forget()
        for i, item in enumerate(self.selected_buttons):
            item.grid_forget()
        self.selected_players_text_box.grid_forget()
        self.player_entry_box.grid_forget()
        self.end_selection_button.grid_forget()
        for i, item in enumerate(self.selected_players):
            self.selected_players[i] = item.split(" |", 1)[0]
        self.parent_app.start_role_selection(self.selected_players)

    def load_players(self):
        self.player_list = []
        with open("../CustomMatchmakerBOT/players.json") as f:
            self.player_data = json.load(f)
        for item in self.player_data:
            self.player_list.append(f"{item} | {self.player_data[item]['name']}")

    def select_player(self, player):
        selected = player.get()
        if "|" in selected and len(self.selected_players) < 10:
            self.selected_players.append(selected)
            self.search_player("")
            self.player_entry_box.delete(0, "end")
            self.refresh_selected_players()
        if len(self.selected_players) == 10:
            self.end_selection_button.configure(state="normal", fg_color="#308019", hover_color="#3ab524",
                                                text="Role Selection →")

    def remove_player(self, player):
        self.selected_players.remove(player.get())
        self.refresh_selected_players()
        self.search_player(self.player_entry_box.get())
        self.end_selection_button.configure(state="disabled", fg_color="#212121", hover_color="#242424",
                                            text="Select more players")

    def refresh_selected_players(self):
        for i in range(10):
            self.selected_vars[i].set("")
        for i in range(len(self.selected_players)):
            self.selected_vars[i].set(self.selected_players[i])

    def search_player(self, text):
        self.query_players = []
        for i in range(8):
            self.query_vars[i].set("")
        if text != "":
            for item in self.player_list:
                if text.lower() in item.lower():
                    self.query_players.append(item)
        else:
            self.query_players = []
        self.query_players = [x for x in self.query_players if x not in self.selected_players]
        if len(self.query_players) > 8:
            self.query_players = self.query_players[:8]
        for i in range(len(self.query_players)):
            self.query_vars[i].set(self.query_players[i])
