import customtkinter as ctk
from db import cursor
import matplotlib.pyplot as plt


def dashboard_screen(main_area, clear_main):
    clear_main()

    # FETCH STATS FROM DB
    cursor.execute("SELECT COUNT(*) FROM events")
    total_events = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM events WHERE event_date > CURDATE()")
    upcoming_events = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM events WHERE event_date < CURDATE()")
    completed_events = cursor.fetchone()[0]

    # TITLE
    ctk.CTkLabel(
        main_area,
        text="Dashboard Overview",
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    # STATS CARDS
    cards_frame = ctk.CTkFrame(main_area, fg_color="transparent")
    cards_frame.pack(pady=10)

    def stat_card(parent, title, value, color):
        card = ctk.CTkFrame(parent, width=180, height=100, fg_color=color, corner_radius=15)
        card.grid_propagate(False)
        card.pack_propagate(False)

        ctk.CTkLabel(card, text=title, font=("Arial", 14)).pack(pady=(15, 5))
        ctk.CTkLabel(card, text=value, font=("Arial", 20, "bold")).pack()
        return card

    stat_card(cards_frame, "Total Events", total_events, "#2a2d3e").grid(row=0, column=0, padx=10)
    stat_card(cards_frame, "Total Users", total_users, "#2a2d3e").grid(row=0, column=1, padx=10)
    stat_card(cards_frame, "Upcoming Events", upcoming_events, "#2a2d3e").grid(row=0, column=2, padx=10)
    stat_card(cards_frame, "Completed Events", completed_events, "#2a2d3e").grid(row=0, column=3, padx=10)

    # EVENT STATUS LIST
    ctk.CTkLabel(
        main_area,
        text="Event Status",
        font=("Arial", 18, "bold")
    ).pack(pady=(25, 10))

    list_box = ctk.CTkTextbox(main_area, width=700, height=150)
    list_box.pack(pady=5)

    cursor.execute("""
        SELECT title,
        CASE
            WHEN event_date > CURDATE() THEN 'Upcoming'
            WHEN event_date = CURDATE() THEN 'Ongoing'
            ELSE 'Completed'
        END AS status
        FROM events
        ORDER BY event_date
    """)

    for title, status in cursor.fetchall():
        list_box.insert("end", f"{title:<30}  →  {status}\n")

    list_box.configure(state="disabled")

    # GRAPH FUNCTION 
    def show_rating_graph():
        cursor.execute("""
            SELECT e.title, ROUND(AVG(f.rating),2)
            FROM feedback f
            JOIN events e ON f.event_id = e.event_id
            GROUP BY e.title
            ORDER BY AVG(f.rating) DESC
        """)

        data = cursor.fetchall()
        if not data:
            return

        events = [row[0] for row in data]
        ratings = [row[1] for row in data]

        plt.figure(figsize=(7, 4))
        plt.bar(events, ratings)
        plt.title("Top Rated Events")
        plt.ylabel("Average Rating")
        plt.xticks(rotation=25)
        plt.tight_layout()
        plt.show()

    # GRAPH BUTTON
    ctk.CTkButton(
        main_area,
        text="Show Top Rated Events Graph",
        command=show_rating_graph,
        width=250
    ).pack(pady=15)