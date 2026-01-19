import customtkinter as ctk
from PIL import Image

from dashboard import dashboard_screen
from events import view_events, add_event, update_event, delete_event
from users import show_users
from feedback import feedback_screen



# APP THEME
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

# APP WINDOW
app = ctk.CTk()
app.geometry("1100x650")
app.title("University Event Management System")

# SIDEBAR
sidebar = ctk.CTkFrame(
    app,
    width=230,
    fg_color="#1f2937"  
)
sidebar.pack(side="left", fill="y")

# Logo
logo_img = ctk.CTkImage(
    Image.open("assets/logo1.png"),
    size=(120, 120)
)
ctk.CTkLabel(sidebar, image=logo_img, text="").pack(pady=20)

ctk.CTkLabel(
    sidebar,
    text="Uni Events",
    font=("Arial", 20, "bold"),
    text_color="white"
).pack(pady=(0, 20))

# MAIN AREA
main_area = ctk.CTkFrame(
    app,
    fg_color="#111827"   # dark background but text visible
)
main_area.pack(side="right", expand=True, fill="both")

# CLEAR MAIN AREA
def clear_main():
    for widget in main_area.winfo_children():
        widget.destroy()

# SIDEBAR BUTTON STYLE
def sidebar_button(text, command):
    return ctk.CTkButton(
        sidebar,
        text=text,
        command=command,
        width=190,
        height=38,
        corner_radius=8,
        fg_color="#2563eb",
        hover_color="#1d4ed8",
        text_color="white"
    )

# SIDEBAR BUTTONS
sidebar_button(
    "📊 Dashboard",
    lambda: dashboard_screen(main_area, clear_main)
).pack(pady=6)

sidebar_button(
    "📅 View Events",
    lambda: view_events(main_area, clear_main)
).pack(pady=6)

sidebar_button(
    "➕ Add Event",
    lambda: add_event(main_area, clear_main)
).pack(pady=6)

sidebar_button(
    "✏️ Update Event",
    lambda: update_event(main_area, clear_main)
).pack(pady=6)

sidebar_button(
    "🗑 Delete Event",
    lambda: delete_event(main_area, clear_main)
).pack(pady=6)

sidebar_button(
    "👥 Manage Users",
    lambda: show_users(main_area, clear_main)
).pack(pady=6)

sidebar_button(
    "⭐ Feedback",
    lambda: feedback_screen(main_area, clear_main)
).pack(pady=6)

# LOAD DEFAULT SCREEN
dashboard_screen(main_area, clear_main)

# RUN APP
app.mainloop()
