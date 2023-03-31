import customtkinter as ct


class RoleSelection:
    def __init__(self, app):
        self.parent_app = app

        self.roles = ["Top", "Jungle", "Mid", "Bot", "Support"]
        self.role_switch_var = []
        self.role_switch = []
        self.role_icon_label = {}

        self.roles_per_player = {}
        self.players_per_role = {
            "Top": [0], "Jungle": [0], "Mid": [0], "Bot": [0], "Support": [0]
        }
        self.available_roles = {
            "Top": [0], "Jungle": [0], "Mid": [0], "Bot": [0], "Support": [0]
        }

        self.role_frame = ct.CTkFrame(master=self.parent_app, width=150, height=400)
        self.role_frame.grid_propagate(False)
        for i in range(7):
            self.role_frame.columnconfigure(i, weight=1)
            self.role_frame.rowconfigure(i, weight=1)

        self.player_segment_button = ct.CTkSegmentedButton(master=self.parent_app, values=["Null"],
                                                           command=self.select_player, dynamic_resizing=False,
                                                           height=50, width=1200, font=("Bahnschrift", 17))
        self.player_name_text = ct.CTkLabel(master=self.parent_app, text="", width=400, height=45,
                                            font=("Bahnschrift", 30))
        self.player_role_submit = ct.CTkButton(master=self.parent_app, text="Submit Roles →", width=350, height=40,
                                               font=("Bahnschrift", 20), fg_color="#308019", hover_color="#3ab524",
                                               state="disabled", command=self.submit_player_roles)
        for i, item in enumerate(self.roles):
            self.role_switch_var.append(ct.StringVar(value=f"{item} 0"))
            self.role_switch.append(ct.CTkSwitch(master=self.role_frame, text="",
                                                 command=lambda x=i: self.role_switch_event(self.role_switch_var[x]),
                                                 variable=self.role_switch_var[i],
                                                 onvalue=f"{item} 1", offvalue=f"{item} 0"))
            self.role_icon_label[item] = ct.CTkLabel(master=self.role_frame, text="",
                                                     image=self.parent_app.disabled_icons[item])

    def start_role_selection(self, players):
        self.role_frame.grid(row=3, column=2, rowspan=9, columnspan=2)
        for i, item in enumerate(self.role_icon_label):
            self.role_switch[i].grid(row=1 + i, column=5)
            self.role_icon_label[item].grid(row=1 + i, column=5, columnspan=2)

        self.player_role_submit.grid(row=9, column=4, columnspan=2)
        self.player_name_text.configure(text=players[0])
        self.player_name_text.grid(row=3, column=1, columnspan=4)
        self.player_segment_button.configure(values=players)
        self.player_segment_button.grid(row=12, column=1, columnspan=12)

    def end_role_selection(self):
        pass

    def select_player(self, value):
        self.player_name_text.configure(text=value)

    def submit_player_roles(self):
        pass

    def check_valid_role(self):
        pass

    def role_switch_event(self, data):
        data = data.get().split(" ")
        if int(data[1]):
            self.role_icon_label[data[0]].configure(image=self.parent_app.enabled_icons[data[0]])
        else:
            self.role_icon_label[data[0]].configure(image=self.parent_app.disabled_icons[data[0]])

    def disable_role(self, role):
        role_index = self.roles.index(role)
        self.role_switch[role_index].grid_forget()
        self.role_icon_label[role].grid_forget()

    def enable_role(self, role):
        role_index = self.roles.index(role)
        self.role_switch[role_index].grid(row=1 + role_index, column=5)
        self.role_icon_label[role].grid(row=1 + role_index, column=5, columnspan=2)

