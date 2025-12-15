import ipapi
from CTkMessagebox import CTkMessagebox
from CTkDatePicker import CTkDatePicker
from customtkinter import *
import actions

FONT = ("arial", 20)
MFONT = ("arial", 17)
GRAPHS = ""

class Interface:

    def __init__(self):
        self.username = ""
        self.token = ""
        self.graphs = []

        self.root = CTk()
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.title("Pixela Habit Tracker")
        self.root.config(padx=30, pady=30)

        self.login()

        actions_frame = CTkFrame(self.root)
        actions_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        new_graph_btn = CTkButton(actions_frame, text="Create New Graph", width=200 , height=50, command=self.create_new_graph)
        new_graph_btn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        delete_graph_btn = CTkButton(actions_frame, text="Delete Graph", width=200 , height=50, command=self.delete_graph)
        delete_graph_btn.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        submit_btn = CTkButton(actions_frame, text="Submit Progress", width=200 , height=50, command=self.submit_progress)
        submit_btn.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        remove_btn = CTkButton(actions_frame, text="Remove Progress", width=200 , height=50, command=self.remove_progress)
        remove_btn.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.root.mainloop()

    def login(self):
        self.root.withdraw()
        popup = CTkToplevel(self.root)
        popup.title("Enter Your Info")
        popup.geometry("700x500")

        login_frame = CTkFrame(popup)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        token_label = CTkLabel(login_frame, text="Token:  ", font=FONT)
        token_label.grid(row=0, column=0)
        token_entry = CTkEntry(login_frame, width=200 , height=50, font=FONT)
        token_entry.grid(row=0, column=1, padx=7, pady=7)

        username_label = CTkLabel(login_frame, text="Username:  ", font=FONT)
        username_label.grid(row=1, column=0)
        username_entry = CTkEntry(login_frame, width=200 , height=50, font=FONT)
        username_entry.grid(row=1, column=1, padx=5, pady=5)

        def submit():
            self.username = username_entry.get().strip()
            self.token = token_entry.get().strip()
            if len(self.username) == 0 or len(self.token) <= 7:
                CTkMessagebox(title="Oops", message="Please make sure that token length at least 8 characters and username not empty.", font=MFONT)
            else:
                actions.headers_value(self.token)
                result = actions.check_user(self.username)
                if result == "no internet connection":
                    return
                elif result:
                    self.graphs = actions.load_graphs(self.username)
                    popup.destroy()
                    self.root.deiconify()
                else:
                    CTkMessagebox(title="ops", message="Username or Token is invalid.\nPlease try again.", font=MFONT)


        def signup():
            self.username = username_entry.get().strip()
            self.token = token_entry.get().strip()
            if len(self.username) == 0 or len(self.token) <= 7:
                CTkMessagebox(title="Oops", message="Please make sure that token length at least 8 characters and username not empty.", font=MFONT)
            else:
                actions.headers_value(self.token)
                result = actions.create_user(self.username, self.token)
                if result == "no internet connection":
                    return
                elif result:
                    popup.destroy()
                    self.root.deiconify()
                else:
                    CTkMessagebox(title="Oops", message="This username already exist.", font=MFONT)

        signup_button = CTkButton(login_frame, text="Signup", command=signup, height=50, font=FONT)
        signup_button.grid(row=3, column=0, sticky="ew", padx=7)

        login_button = CTkButton(login_frame, text="Login", command=submit, height=50, font=FONT)
        login_button.grid(row=3, column=1, sticky="ew", padx=7, pady=7)

        popup.grab_set()
        popup.focus_set()
        popup.wait_window()

    def create_new_graph(self):
        self.root.withdraw()
        popup = CTkToplevel(self.root)
        popup.title("Create new graph")
        popup.geometry("500x500")

        new_graph_frame = CTkFrame(popup)
        new_graph_frame.place(relx=0.5, rely=0.5, anchor="center")

        graph_id_label = CTkLabel(new_graph_frame, text="Id:  ", font=FONT)
        graph_id_label.grid(row=0, column=0)
        graph_id_entry = CTkEntry(new_graph_frame, width=200 , height=50, font=FONT)
        graph_id_entry.grid(row=0, column=2, padx=7, pady=7)

        graph_name_label = CTkLabel(new_graph_frame, text="Name:  ", font=FONT)
        graph_name_label.grid(row=1, column=0, padx=10)
        graph_name_entry = CTkEntry(new_graph_frame, width=200 , height=50, font=FONT)
        graph_name_entry.grid(row=1, column=2, pady=5)

        unit_label = CTkLabel(new_graph_frame, text="Unit:  ", font=FONT)
        unit_label.grid(row=2, column=0)
        unit_entry = CTkEntry(new_graph_frame, width=200 , height=50, font=FONT)
        unit_entry.grid(row=2, column=2, pady=5)

        graph_type_label = CTkLabel(new_graph_frame, text="Type:  ", font=FONT)
        graph_type_label.grid(row=3, column=0)
        graph_type_segment = CTkSegmentedButton(new_graph_frame, values=["int", "float"], height=50, corner_radius=10, font=FONT)
        graph_type_segment.grid(row=3, column=2, padx=7, pady=5, sticky="ew")

        def color_change(choice):
            colors = {"shibafu": "green", "momiji": "#ba2227", "sora": "#4136d1", "ichou": "#aba424", "ajisai": "purple", "kuro": "black"}
            graph_color_options.configure(fg_color=colors[choice])
            graph_color_options.configure(button_color=colors[choice])

        graph_color_label = CTkLabel(new_graph_frame, text="Color:  ", font=FONT)
        graph_color_label.grid(row=4, column=0)
        graph_color_options = CTkOptionMenu(new_graph_frame,
                                            values=["shibafu", "momiji", "sora", "ichou", "ajisai", "kuro"],
                                            height=40,
                                            dropdown_font=("arial", 20),
                                            font=("arial", 20, "bold"),
                                            fg_color="green",
                                            button_color="green",
                                            hover=False,
                                            anchor=CENTER,
                                            command=color_change)
        graph_color_options.grid(row=4, column=2, padx=7, pady=5, sticky="ew")


        def get_timezone():
            timezone = ipapi.location(output="timezone")
            graph_timezone_entry.delete(0, END)
            graph_timezone_entry.insert(0, timezone)

        graph_timezone_label = CTkLabel(new_graph_frame, text="Timezone:  ", font=FONT)
        graph_timezone_label.grid(row=5, column=0)
        graph_timezone_entry = CTkEntry(new_graph_frame, width=150 , height=50, font=FONT)
        graph_timezone_entry.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        ip_get_button = CTkButton(new_graph_frame, text="Get", width=25, height=50, font=FONT, command=get_timezone)
        ip_get_button.grid(row=5, column=2, padx=7, sticky="e")

        def submit():
            graph_id = graph_id_entry.get().strip()
            graph_name = graph_name_entry.get().strip()
            unit = unit_entry.get().strip()
            graph_type = graph_type_segment.get()
            graph_color = graph_color_options.get()
            timezone = graph_timezone_entry.get()
            if len(graph_id) == 0 or len(graph_name) == 0 or len(unit) == 0 or len(graph_type) == 0:
                CTkMessagebox(title="Oops", message="Please make sure you haven't left any fields empty.", font=MFONT)
            else:
                result = actions.create_graph(graph_id, graph_name, unit, graph_type, graph_color, timezone, self.username)
                if result == "no internet connection":
                    return
                elif not result:
                    CTkMessagebox(title="Oops", message="This graph id already exist.")
                else:
                    self.graphs.append(graph_id)
                    CTkMessagebox(title="", message="Graph has been created successfully.", font=MFONT, icon="check")
                    back()

        def back():
            popup.destroy()
            self.root.deiconify()

        back_button = CTkButton(new_graph_frame, text="Back", command=back, height=50, font=FONT)
        back_button.grid(row=6, column=0, sticky="ew", padx=7, pady=7)

        submit_button = CTkButton(new_graph_frame, text="Submit", command=submit, height=50, font=FONT)
        submit_button.grid(row=6, column=2, sticky="ew", padx=7, pady=7)


    def delete_graph(self):
        self.root.withdraw()
        popup = CTkToplevel(self.root)
        popup.title("Delete graph")
        popup.geometry("500x500")

        delete_graph_frame = CTkFrame(popup)
        delete_graph_frame.place(relx=0.5, rely=0.5, anchor="center")

        graph_id_label = CTkLabel(delete_graph_frame, text="Id:  ", font=FONT)
        graph_id_label.grid(row=0, column=0, padx=7)
        graph_id_options = CTkOptionMenu(delete_graph_frame,
                                       values=self.graphs,
                                       width=200,
                                       height=40,
                                       dropdown_font=("arial", 20),
                                       font=("arial", 20, "bold"),
                                       hover=False,
                                       anchor=CENTER
                                       )
        graph_id_options.grid(row=0, column=1, padx=7, pady=7)
        graph_id_options.set("Select a graph")
        def submit():
            graph_id = graph_id_options.get().strip()
            if graph_id == "Select a graph":
                CTkMessagebox(title="Oops", message="Please select a graph to delete.", icon="warning", font=MFONT)
            else:
                msg = CTkMessagebox(title="Delete graph", message="Are you sure?", font=MFONT, icon="question",
                                    option_1="Cancel", option_2="Yes")
                if msg.get() == "Yes":
                    result = actions.delete_graph(self.username, graph_id)
                    if result == "no internet connection":
                        return
                    # elif not result:
                    #     CTkMessagebox(title="Oops", message="This graph id doesn't exist.", font=MFONT)
                    else:
                        self.graphs.remove(graph_id)
                        CTkMessagebox(title="", message="Graph has been deleted successfully.", font=MFONT, icon="check")
                        back()

        def back():
            popup.destroy()
            self.root.deiconify()

        back_button = CTkButton(delete_graph_frame, text="Back", command=back, height=50, font=FONT)
        back_button.grid(row=1, column=0, sticky="ew", padx=7, pady=7)

        submit_button = CTkButton(delete_graph_frame, text="Submit", command=submit, height=50, font=FONT)
        submit_button.grid(row=1, column=1, sticky="ew", padx=7, pady=7)

        if not self.graphs: # if user have no graph
            graph_id_options.set("No graphs available")
            submit_button.configure(state="disabled")

    def submit_progress(self):
        self.root.withdraw()
        popup = CTkToplevel(self.root)
        popup.title("Add progress")
        popup.geometry("500x500")

        submit_progress_frame = CTkFrame(popup)
        submit_progress_frame.place(relx=0.5, rely=0.5, anchor="center")

        graph_id_label = CTkLabel(submit_progress_frame, text="Id:  ", font=FONT)
        graph_id_label.grid(row=0, column=0)
        graph_id_options = CTkOptionMenu(submit_progress_frame,
                                         values=self.graphs,
                                         width=200,
                                         height=40,
                                         dropdown_font=("arial", 20),
                                         font=("arial", 20, "bold"),
                                         hover=False,
                                         anchor=CENTER
                                         )
        graph_id_options.grid(row=0, column=1, padx=7, pady=7, sticky="ew")
        graph_id_options.set("Select a graph")

        date_label = CTkLabel(submit_progress_frame, text="Date:  ", font=FONT)
        date_label.grid(row=1, column=0, padx=7)
        calendar = CTkDatePicker(submit_progress_frame)
        calendar.grid(row=1, column=1, padx=7, pady=5, sticky="ew")

        quantity_label = CTkLabel(submit_progress_frame, text=" Quantity:  ", font=FONT)
        quantity_label.grid(row=2, column=0, padx=7)
        quantity_entry = CTkEntry(submit_progress_frame, width=200 , height=50, font=FONT)
        quantity_entry.grid(row=2, column=1, padx=7, pady=5, sticky="ew")

        def submit():
            graph_id = graph_id_options.get().strip()
            date = "".join(calendar.get_date().split("/")[::-1])
            quantity = quantity_entry.get().strip()
            if graph_id == "Select a graph" or len(date) == 0 or len(quantity) == 0:
                CTkMessagebox(title="Oops", message="Please make sure you  haven't left any fields empty.", font=MFONT)
            else:
                result = actions.add_pixel(date, quantity, self.username, graph_id)
                if result == "no internet connection":
                    return
                elif not result:
                    CTkMessagebox(title="Oops", message="Invalid quantity type.\nOnly numbers accepted", icon="warning", font=MFONT)
                else:
                    CTkMessagebox(title="", message="Progress has been applied successfully.", font=MFONT, icon="check")
                    back()

        def back():
            popup.destroy()
            self.root.deiconify()

        back_button = CTkButton(submit_progress_frame, text="Back", command=back, height=50, font=FONT)
        back_button.grid(row=3, column=0, sticky="ew", padx=7, pady=7)

        submit_button = CTkButton(submit_progress_frame, text="Submit", command=submit, height=50, font=FONT)
        submit_button.grid(row=3, column=1, columnspan=5, sticky="ew", padx=7, pady=7)

        if not self.graphs: # if user have no graph
            graph_id_options.set("No graphs available")
            submit_button.configure(state="disabled")

    def remove_progress(self):
        self.root.withdraw()
        popup = CTkToplevel(self.root)
        popup.title("Remove progress")
        popup.geometry("500x500")

        remove_progress_frame = CTkFrame(popup)
        remove_progress_frame.place(relx=0.5, rely=0.5, anchor="center")

        graph_id_label = CTkLabel(remove_progress_frame, text="Id:  ", font=FONT)
        graph_id_label.grid(row=0, column=0)

        graph_id_options = CTkOptionMenu(remove_progress_frame,
                                         values=self.graphs,
                                         width=200,
                                         height=40,
                                         dropdown_font=("arial", 20),
                                         font=("arial", 20, "bold"),
                                         hover=False,
                                         anchor=CENTER
                                         )
        graph_id_options.grid(row=0, column=1, padx=7, pady=7, sticky="ew")
        graph_id_options.set("Select a graph")

        date_label = CTkLabel(remove_progress_frame, text="Date:  ", font=FONT)
        date_label.grid(row=1, column=0, padx=7)
        calendar = CTkDatePicker(remove_progress_frame)
        calendar.grid(row=1, column=1, padx=7, pady=5, sticky="ew")

        def submit():
            graph_id = graph_id_options.get().strip()
            date = "".join(calendar.get_date().split("/")[::-1])
            if graph_id == "Select a graph" or len(date) == 0:
                CTkMessagebox(title="Oops", message="Please make sure you haven't left any fields empty.", font=MFONT)
            else:
                msg = CTkMessagebox(title="Remove progress", message="Are you sure?", font=MFONT, icon="question",
                              option_1="Cancel", option_2="Yes")
                if msg.get() == "Yes":
                    result = actions.delete_pixel(self.username, graph_id, date)
                    if result == "no internet connection":
                        return
                    elif not result:
                        CTkMessagebox(title="Oops", message="Empty progress for this date.", font=MFONT)
                    else:
                        CTkMessagebox(title="", message="Progress has been removed successfully.", font=MFONT, icon="check")
                        back()

        def back():
            popup.destroy()
            self.root.deiconify()

        back_button = CTkButton(remove_progress_frame, text="Back", command=back, height=50, font=FONT)
        back_button.grid(row=2, column=0, sticky="ew", padx=7, pady=7)

        submit_button = CTkButton(remove_progress_frame, text="Submit", command=submit, height=50, font=FONT)
        submit_button.grid(row=2, column=1, columnspan=5, sticky="ew", padx=7, pady=7)

        if not self.graphs: # if user have no graph
            graph_id_options.set("No graphs available")
            submit_button.configure(state="disabled")