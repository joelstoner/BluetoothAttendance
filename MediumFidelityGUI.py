import tkinter as tk

class LoginScreen(tk.Frame):
    def __init__(self, master, on_success):
        super().__init__(master, bg="#333333")
        self.on_success = on_success

        self.pack(expand=True, fill="both")
        content = tk.Frame(self, bg="#333333")
        content.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(content, text="Welcome to Bluettend!", fg="#1E90FF", bg="#333333", font=("Helvetica", 16, "bold")).pack()
        tk.Label(content, text="Username", bg="#333333", fg="#ffffff").pack()
        self.username = tk.Entry(content, bg="#4f4f4f", fg="#ffffff", insertbackground="white")
        self.username.pack(fill="x")
        tk.Label(content, text="Password", bg="#333333", fg="#ffffff").pack()
        self.password = tk.Entry(content, show="*", bg="#4f4f4f", fg="#ffffff", insertbackground="white")
        self.password.pack(fill="x")
        login_btn = tk.Button(content, text="Login", bg="#555555", fg="#ffffff", command=self._login)
        login_btn.pack(pady=10)

    def _login(self):
        print("Attempting login with:", self.username.get(), self.password.get())
        self.on_success()

class SettingsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#333333")
        self.pack(expand=True, fill="both")

        self.create_section("User Profile")
        self.create_option("Username", "Change your username.")
        self.create_option("Password", "Update your password.")
        
        self.create_section("Notifications")
        self.create_toggle_option("Email Notifications", True)
        self.create_toggle_option("Push Notifications", False)
        
        self.create_section("Appearance")
        self.create_toggle_option("Dark Mode", False)
        
        self.create_section("Privacy & Security")
        self.create_toggle_option("Two-factor Authentication", False)
        
        self.create_section("Language & Region")
        self.create_option("Language", "Select your language.")
        
    def create_section(self, title):
        """Creates a section header."""
        tk.Label(self, text=title, bg="#333333", fg="#1E90FF", font=("Helvetica", 14, "bold")).pack(pady=(10, 5), fill="x", padx=15)
        
    def create_option(self, title, description):
        """Creates a simple option with a description."""
        frame = tk.Frame(self, bg="#444444", bd=1)
        frame.pack(padx=15, pady=5, fill="x", expand=True)
        
        tk.Label(frame, text=title, bg="#444444", fg="#ffffff", font=("Helvetica", 12, "bold")).pack(anchor="w", padx=5)
        tk.Label(frame, text=description, bg="#444444", fg="#aaaaaa", font=("Helvetica", 10)).pack(anchor="w", padx=5)
        
    def create_toggle_option(self, title, is_enabled):
        """Creates a toggleable option."""
        frame = tk.Frame(self, bg="#444444", bd=1)
        frame.pack(padx=15, pady=5, fill="x", expand=True)
        
        tk.Label(frame, text=title, bg="#444444", fg="#ffffff", font=("Helvetica", 12, "bold")).pack(side="left", padx=5)
        
        toggle = tk.StringVar(value="On" if is_enabled else "Off")
        tk.Button(frame, textvariable=toggle, command=lambda: self.toggle_option(toggle),
                  bg="#555555", fg="#ffffff", font=("Helvetica", 10)).pack(side="right", padx=5)
        
    def toggle_option(self, toggle_var):
        """Toggles the option on or off."""
        toggle_var.set("Off" if toggle_var.get() == "On" else "On")



class ClassList(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#333333")
        self.pack(expand=True, fill="both")
        
        # Adding the title at the top of the ClassList page
        tk.Label(self, text="ClassList", bg="#333333", fg="#1E90FF", font=("Helvetica", 18, "bold")).pack(pady=(10, 20))
        
        canvas = tk.Canvas(self, borderwidth=0, background="#333333")
        self.scrollable_frame = tk.Frame(canvas, bg="#333333")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas_frame = canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_frame, width=e.width))

        for i in range(1, 4):
            item_frame = tk.Frame(self.scrollable_frame, bg="#555555", bd=2)
            item_frame.pack(padx=10, pady=5, fill="x", expand=True)

            # Your existing label
            tk.Label(item_frame, text=f"Class {i}\nXX:XX-XX:XX\nAttendance: 100%", bg="#555555", fg="#ffffff", justify=tk.LEFT).pack(side="left", padx=10)

            # Canvas for the status indicator
            status_canvas = tk.Canvas(item_frame, bg="#555555", height=20, width=20, bd=0, highlightthickness=0)
            status_canvas.pack(side="right", padx=10, pady=10)

            # Decide the color based on some condition. Here, just randomly choosing one for demonstration.
            color = "green" if i % 2 == 0 else "red"
    
            # Drawing the circle
            status_canvas.create_oval(2, 2, 18, 18, fill=color, outline=color)


class ClassRoster(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#333333")
        self.pack(expand=True, fill="both")

        # Frame for the title and buttons
        title_frame = tk.Frame(self, bg="#333333")
        title_frame.pack(side="top", fill="x", pady=(10, 20))

        # Edit button on the left
        edit_button = tk.Button(title_frame, text="Edit", command=self.edit_action, bg="#555555", fg="#ffffff")
        edit_button.pack(side="left", padx=10)

        # ClassRoster title in the center
        tk.Label(title_frame, text="ClassRoster", bg="#333333", fg="#1E90FF", font=("Helvetica", 18, "bold")).pack(side="left", expand=True)

        # Submit button on the right
        submit_button = tk.Button(title_frame, text="Submit", command=self.submit_action, bg="#555555", fg="#ffffff")
        submit_button.pack(side="right", padx=10)

        # Canvas setup
        canvas = tk.Canvas(self, borderwidth=0, background="#333333")
        self.scrollable_frame = tk.Frame(canvas, bg="#333333")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas_frame = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        # Ensure scrollable_frame expands to fill the canvas
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_frame, width=e.width))

        # Adding students to the roster with a status indicator
        for i in range(1, 21):  # Adjusted for 20 students
            item_frame = tk.Frame(self.scrollable_frame, bg="#555555", bd=2)
            item_frame.pack(padx=10, pady=5, fill="x", expand=True)
            tk.Label(item_frame, text=f"Student {i}", bg="#555555", fg="#ffffff", justify=tk.LEFT).pack(side="left", padx=10)

            # Canvas for the status indicator
            status_canvas = tk.Canvas(item_frame, bg="#555555", height=20, width=20, bd=0, highlightthickness=0)
            status_canvas.pack(side="right", padx=10, pady=10)

            # Decide the color based on some condition, e.g., alternating
            color = "green" if i % 2 == 0 else "red"
            
            # Drawing the circle
            status_canvas.create_oval(2, 2, 18, 18, fill=color, outline=color)

    def edit_action(self):
        # Placeholder for edit action logic
        print("Edit action triggered")

    def submit_action(self):
        # Placeholder for submit action logic
        print("Submit action triggered")


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter App")
        self.geometry("360x640")
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.bottom_frame = tk.Frame(self, bg="#333333")
        self.bottom_frame.pack(side="bottom", fill="x")

        self.login_screen = LoginScreen(self.container, self.after_login)
        self.classlist_screen = None
        self.classroster_screen = None
        self.settings_page = None

    def after_login(self):
        self.login_screen.destroy()
        self._create_bottom_nav()
        self.show_classlist_screen()

    def _create_bottom_nav(self):
        btn_classlist = tk.Button(self.bottom_frame, text="ClassList", bg="#555555", fg="#ffffff", command=self.show_classlist_screen)
        btn_classlist.pack(side="left", expand=True, fill="x")

        btn_classroster = tk.Button(self.bottom_frame, text="ClassRoster", bg="#555555", fg="#ffffff", command=self.show_classroster_screen)
        btn_classroster.pack(side="left", expand=True, fill="x")

        btn_settings = tk.Button(self.bottom_frame, text="Settings", bg="#555555", fg="#ffffff", command=self.show_settings_page)
        btn_settings.pack(side="left", expand=True, fill="x")

    def show_classlist_screen(self):
        if self.classlist_screen:
            self.classlist_screen.destroy()
        if self.classroster_screen:
            self.classroster_screen.destroy()
        if self.settings_page:
            self.settings_page.destroy()

        self.classlist_screen = ClassList(self.container)

    def show_classroster_screen(self):
        if self.classlist_screen:
            self.classlist_screen.destroy()
        if self.classroster_screen:
            self.classroster_screen.destroy()
        if self.settings_page:
            self.settings_page.destroy()

        self.classroster_screen = ClassRoster(self.container)

    def show_settings_page(self):
        if self.classlist_screen:
            self.classlist_screen.destroy()
        if self.classroster_screen:
            self.classroster_screen.destroy()
        if self.settings_page:
            self.settings_page.destroy()
        self.settings_page = SettingsPage(self.container)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
