import customtkinter as ctk
from db import cursor, conn

def feedback_screen(main_area, clear_main):
    clear_main()

    #  ENTRY FIELDS
    uid = ctk.CTkEntry(main_area, placeholder_text="User ID")
    uid.pack(pady=5)

    eid = ctk.CTkEntry(main_area, placeholder_text="Event ID")
    eid.pack(pady=5)

    rating = ctk.CTkEntry(main_area, placeholder_text="Rating (1-5)")
    rating.pack(pady=5)

    comment = ctk.CTkEntry(main_area, placeholder_text="Comment")
    comment.pack(pady=5)

    msg = ctk.CTkLabel(main_area, text="")
    msg.pack()

    #  TEXTBOX 
    box = ctk.CTkTextbox(main_area, width=650, height=250)
    box.pack(pady=10)

    #  SUBMIT FEEDBACK 
    def submit_feedback():
        msg.configure(text="", text_color="white")

        # rating validation
        try:
            r = int(rating.get())
            if r < 1 or r > 5:
                msg.configure(text="Rating must be between 1 and 5", text_color="red")
                return
        except:
            msg.configure(text="Rating must be a number", text_color="red")
            return

        try:
            cursor.execute(
                "INSERT INTO feedback(user_id, event_id, rating, comments) VALUES (%s,%s,%s,%s)",
                (uid.get(), eid.get(), r, comment.get())
            )
            conn.commit()

            msg.configure(text="Feedback submitted successfully!", text_color="green")

            # clear entries
            uid.delete(0, "end")
            eid.delete(0, "end")
            rating.delete(0, "end")
            comment.delete(0, "end")

            load_feedback()

        except Exception as e:
            msg.configure(text=f"Error: {e}", text_color="red")
            print("Feedback Error:", e)

    #  LOAD FEEDBACK
    def load_feedback():
        box.delete("1.0", "end")
        try:
            cursor.execute("""
                SELECT e.title, f.rating, f.comments, f.user_id
                FROM feedback f
                JOIN events e ON f.event_id = e.event_id
                ORDER BY e.event_date DESC
            """)
            for row in cursor.fetchall():
                box.insert(
                    "end",
                    f"Event: {row[0]} | UserID: {row[3]} | Rating: {row[1]} | Comment: {row[2]}\n"
                )
        except Exception as e:
            box.insert("end", f"Error loading feedback: {e}")

    #  AVG RATING 
    def avg_rating():
        box.delete("1.0", "end")
        try:
            cursor.execute("""
                SELECT e.title, ROUND(AVG(f.rating),2)
                FROM feedback f
                JOIN events e ON f.event_id = e.event_id
                GROUP BY e.title
                ORDER BY 2 DESC
            """)
            for row in cursor.fetchall():
                box.insert("end", f"Event: {row[0]} | Avg Rating: {row[1]}\n")
        except Exception as e:
            box.insert("end", f"Error: {e}")

    #  BUTTONS 
    ctk.CTkButton(main_area, text="Submit Feedback", command=submit_feedback).pack(pady=5)
    ctk.CTkButton(main_area, text="View All Feedback", command=load_feedback).pack(pady=5)
    ctk.CTkButton(main_area, text="Average Ratings", command=avg_rating).pack(pady=5)

    load_feedback()
