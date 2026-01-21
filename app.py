import streamlit as st
import sqlite3
from datetime import date

# ---------------- DATABASE ---------------- #

def get_connection(db_name="users.db"):
    return sqlite3.connect(db_name)

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                                                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                     first_name TEXT,
                                                     last_name TEXT,
                                                     dob TEXT
                )
                """)
    conn.commit()
    conn.close()

def add_user(first, last, dob):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (first_name, last_name, dob) VALUES (?, ?, ?)",
        (first, last, dob)
    )
    conn.commit()
    conn.close()

def search_users(first, last, dob):
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT * FROM users WHERE 1=1"
    params = []

    if first:
        query += " AND first_name = ?"
        params.append(first)
    if last:
        query += " AND last_name = ?"
        params.append(last)
    if dob:
        query += " AND dob = ?"
        params.append(dob)

    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows

def update_user(user_id, first, last, dob):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                UPDATE users
                SET first_name = ?, last_name = ?, dob = ?
                WHERE id = ?
                """, (first, last, dob, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def fetch_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows

# Initialize DB
create_table()

# ---------------- SIDEBAR (DROPDOWN NAV) ---------------- #

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose an option",
    [
        "Home",
        "Add User",
        "Search User",
        "Edit User",
        "Delete User",
        "Display Database"
    ]
)

# ---------------- PAGES ---------------- #

# HOME
if page == "Home":
    st.title("User Management System")

    st.markdown("""
    ### Purpose
    This application provides a simple interface for managing user records
    using a local SQLite database.

    ### Features
    - Add new users
    - Search users by name or date of birth
    - Edit existing user records
    - Delete users
    - Display all stored users

    ### Technology Stack
    - Python
    - Streamlit
    - SQLite
    """)

# ADD USER
elif page == "Add User":
    st.title("Add User")

    first = st.text_input("First Name")
    last = st.text_input("Last Name")

    dob = st.date_input(
        "Date of Birth",
        min_value=date(1950, 1, 1),
        max_value=date.today()
    )

    if st.button("Add User"):
        if first and last:
            add_user(first, last, str(dob))
            st.success("User added successfully.")
        else:
            st.error("First and last name are required.")

# SEARCH USER
elif page == "Search User":
    st.title("Search User")

    first = st.text_input("First Name (optional)")
    last = st.text_input("Last Name (optional)")
    dob = st.text_input("DOB (YYYY-MM-DD, optional)")

    if st.button("Search"):
        results = search_users(first, last, dob)
        if results:
            st.table(results)
        else:
            st.info("No matching users found.")

# EDIT USER
elif page == "Edit User":
    st.title("Edit User")

    users = fetch_all_users()
    if not users:
        st.info("No users available.")
    else:
        user_map = {
            f"{u[0]}: {u[1]} {u[2]} ({u[3]})": u for u in users
        }

        selected = st.selectbox("Select User", list(user_map.keys()))
        user = user_map[selected]

        new_first = st.text_input("First Name", user[1])
        new_last = st.text_input("Last Name", user[2])
        new_dob = st.text_input("DOB (YYYY-MM-DD)", user[3])

        if st.button("Update User"):
            update_user(user[0], new_first, new_last, new_dob)
            st.success("User updated successfully.")

# DELETE USER
elif page == "Delete User":
    st.title("Delete User")

    users = fetch_all_users()
    if not users:
        st.info("No users available.")
    else:
        user_map = {
            f"{u[0]}: {u[1]} {u[2]} ({u[3]})": u[0] for u in users
        }

        selected = st.selectbox("Select User", list(user_map.keys()))

        if st.button("Delete User"):
            delete_user(user_map[selected])
            st.warning("User deleted.")

# DISPLAY DATABASE
elif page == "Display Database":
    st.title("Database Records")

    data = fetch_all_users()
    if data:
        st.table(data)
    else:
        st.write("Database is empty.")


