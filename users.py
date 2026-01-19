import customtkinter as ctk
from db import cursor, conn

def show_users(main_area, clear_main):
    clear_main()

    #  ENTRY FIELDS 
    name = ctk.CTkEntry(main_area, placeholder_text="Name")
    name.pack(pady=5)

    email = ctk.CTkEntry(main_area, placeholder_text="Email")
    email.pack(pady=5)

    user_id_entry = ctk.CTkEntry(main_area, placeholder_text="User ID (for Update/Delete/Register)")
    user_id_entry.pack(pady=5)

    event_id_entry = ctk.CTkEntry(main_area, placeholder_text="Event ID (for Registration)")
    event_id_entry.pack(pady=5)

    #  TEXTBOX TO DISPLAY USERS 
    box = ctk.CTkTextbox(main_area, width=650, height=250)
    box.pack(pady=10)

    #  FUNCTIONS
    def load_users():
        box.delete("1.0", "end")
        try:
            cursor.execute("SELECT * FROM users ORDER BY user_id")
            for row in cursor.fetchall():
                box.insert("end", f"{row}\n")
        except Exception as e:
            print("Error loading users:", e)

    def add_user():
        try:
            cursor.execute("INSERT INTO users(name,email) VALUES (%s,%s)", (name.get(), email.get()))
            conn.commit()  # commit to DB
            name.delete(0, "end")
            email.delete(0, "end")
            load_users()
            print("User added successfully!")
        except Exception as e:
            print("Error adding user:", e)

    def update_user():
        try:
            cursor.execute("UPDATE users SET name=%s,email=%s WHERE user_id=%s",
                           (name.get(), email.get(), user_id_entry.get()))
            conn.commit()
            load_users()
            print("User updated successfully!")
            # Clear fields
            user_id_entry.delete(0, "end")
            name.delete(0, "end")
            email.delete(0, "end")
        except Exception as e:
            print("Error updating user:", e)

    def delete_user():
        try:
            cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id_entry.get(),))
            conn.commit()
            user_id_entry.delete(0, "end")
            load_users()
            print("User deleted successfully!")
        except Exception as e:
            print("Error deleting user:", e)

    def register_user():
        try:
            cursor.execute("INSERT INTO registrations(user_id,event_id) VALUES (%s,%s)",
                           (user_id_entry.get(), event_id_entry.get()))
            conn.commit()
            event_id_entry.delete(0, "end")
            print("User registered to event successfully!")
        except Exception as e:
            print("Error registering user:", e)

    #  BUTTONS 
    ctk.CTkButton(main_area, text="Add User", command=add_user).pack(pady=3)
    ctk.CTkButton(main_area, text="Update User", command=update_user).pack(pady=3)
    ctk.CTkButton(main_area, text="Delete User", command=delete_user).pack(pady=3)
    ctk.CTkButton(main_area, text="Register User to Event", command=register_user).pack(pady=3)
    ctk.CTkButton(main_area, text="View Users", command=load_users).pack(pady=3)

    #  INITIAL LOAD 
    load_users()
