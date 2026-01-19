import customtkinter as ctk
from db import cursor, conn
from datetime import date

# VIEW / SEARCH / SORT EVENTS
def view_events(main_area, clear_main):
    clear_main()

    # Search Entry
    search = ctk.CTkEntry(main_area, placeholder_text="Search by title or venue")
    search.pack(pady=5)

    # Sort Option
    sort_option = ctk.CTkOptionMenu(
        main_area,
        values=["Sort by Date", "Sort by Venue"]
    )
    sort_option.pack(pady=5)
    sort_option.set("Sort by Date")

    # Textbox to display events
    box = ctk.CTkTextbox(main_area, width=650, height=350)
    box.pack(pady=10)

    # Load events function
    def load_events(query="SELECT * FROM events ORDER BY event_date"):
        box.delete("1.0", "end")
        cursor.execute(query)
        for row in cursor.fetchall():
            # Add status column
            status = ""
            if row[3] > date.today():
                status = "Upcoming"
            elif row[3] == date.today():
                status = "Ongoing"
            else:
                status = "Completed"
            box.insert("end", f"{row} | Status: {status}\n")

    # Search function
    def search_event():
        box.delete("1.0", "end")
        cursor.execute("""
            SELECT * FROM events
            WHERE title LIKE %s OR venue LIKE %s
            ORDER BY event_date
        """, (f"%{search.get()}%", f"%{search.get()}%"))
        for row in cursor.fetchall():
            status = ""
            if row[3] > date.today():
                status = "Upcoming"
            elif row[3] == date.today():
                status = "Ongoing"
            else:
                status = "Completed"
            box.insert("end", f"{row} | Status: {status}\n")

    # Sort function
    def sort_events():
        if sort_option.get() == "Sort by Venue":
            load_events("SELECT * FROM events ORDER BY venue")
        else:
            load_events("SELECT * FROM events ORDER BY event_date")

    # Buttons
    ctk.CTkButton(main_area, text="Search", command=search_event).pack(pady=3)
    ctk.CTkButton(main_area, text="Sort", command=sort_events).pack(pady=3)

    load_events()

# ==============================
# ADD EVENT

def add_event(main_area, clear_main):
    clear_main()

    frame = ctk.CTkFrame(main_area, fg_color=main_area.cget("fg_color"), corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor="center")  

    title = ctk.CTkEntry(frame, placeholder_text="Event Title", width=400, height=35)
    title.pack(pady=10)

    venue = ctk.CTkEntry(frame, placeholder_text="Venue", width=400, height=35)
    venue.pack(pady=10)

    event_date = ctk.CTkEntry(frame, placeholder_text="YYYY-MM-DD", width=400, height=35)
    event_date.pack(pady=10)

    msg_label = ctk.CTkLabel(frame, text="", text_color="green", font=("Arial", 12))
    msg_label.pack(pady=5)

    def save_event():
        try:
            cursor.execute(
                "INSERT INTO events(title, venue, event_date) VALUES (%s,%s,%s)",
                (title.get(), venue.get(), event_date.get())
            )
            conn.commit()

            # Clear entries
            title.delete(0, "end")
            venue.delete(0, "end")
            event_date.delete(0, "end")

            # Show success message
            msg_label.configure(text="Event added successfully!")

        except Exception as e:
            msg_label.configure(text=f"Error: {e}", text_color="red")

    # SAVE BUTTON 
    ctk.CTkButton(frame, text="Save Event", command=save_event, width=200, height=40).pack(pady=15)



# UPDATE EVENT
def update_event(main_area, clear_main):
    clear_main()

    frame = ctk.CTkFrame(main_area, fg_color=main_area.cget("fg_color"), corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    event_id = ctk.CTkEntry(frame, placeholder_text="Event ID", width=400, height=35)
    event_id.pack(pady=10)

    title = ctk.CTkEntry(frame, placeholder_text="New Title", width=400, height=35)
    title.pack(pady=10)

    venue = ctk.CTkEntry(frame, placeholder_text="New Venue", width=400, height=35)
    venue.pack(pady=10)

    event_date = ctk.CTkEntry(frame, placeholder_text="YYYY-MM-DD", width=400, height=35)
    event_date.pack(pady=10)

    msg_label = ctk.CTkLabel(frame, text="", font=("Arial", 12))
    msg_label.pack(pady=5)

    def update():
        try:
            cursor.execute("""
                UPDATE events
                SET title=%s, venue=%s, event_date=%s
                WHERE event_id=%s
            """, (title.get(), venue.get(), event_date.get(), event_id.get()))
            conn.commit()

            # Clear entries
            event_id.delete(0, "end")
            title.delete(0, "end")
            venue.delete(0, "end")
            event_date.delete(0, "end")

            msg_label.configure(text="Event updated successfully!", text_color="green")

        except Exception as e:
            msg_label.configure(text=f"Error: {e}", text_color="red")

    ctk.CTkButton(frame, text="Update Event", command=update, width=200, height=40).pack(pady=15)


# DELETE EVENT
def delete_event(main_area, clear_main):
    clear_main()

    frame = ctk.CTkFrame(main_area, fg_color=main_area.cget("fg_color"), corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    event_id = ctk.CTkEntry(frame, placeholder_text="Event ID", width=400, height=35)
    event_id.pack(pady=15)

    msg_label = ctk.CTkLabel(frame, text="", font=("Arial", 12))
    msg_label.pack(pady=5)

    def delete():
        try:
            cursor.execute("DELETE FROM events WHERE event_id=%s", (event_id.get(),))
            conn.commit()
            event_id.delete(0, "end")
            msg_label.configure(text="Event deleted successfully!", text_color="green")
        except Exception as e:
            msg_label.configure(text=f"Error: {e}", text_color="red")

    ctk.CTkButton(frame, text="Delete Event", command=delete, width=200, height=40).pack(pady=20)
