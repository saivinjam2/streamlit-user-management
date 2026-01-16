import os
import sqlite3
import pytest
import app
app.DB_NAME = "test_users.db"

from app import (
    get_connection,
    create_table,
    add_user,
    fetch_all_users,
    search_users,
    update_user,
    delete_user
)

TEST_DB = "test_users.db"

# ---------------- FIXTURE ---------------- #

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Create clean test database
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    conn = get_connection(TEST_DB)
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE users (
                                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                                       first_name TEXT,
                                       last_name TEXT,
                                       dob TEXT
                )
                """)
    conn.commit()
    conn.close()

    yield

    # Cleanup
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

# ---------------- TESTS ---------------- #

def test_add_user():
    add_user("John", "Doe", "2000-01-01")

    conn = get_connection(TEST_DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()

    assert len(rows) == 1
    assert rows[0][1] == "John"
    assert rows[0][2] == "Doe"


def test_fetch_all_users():
    add_user("Alice", "Smith", "1999-05-05")
    add_user("Bob", "Brown", "1998-03-03")

    rows = fetch_all_users()
    assert len(rows) == 2


def test_search_users_partial_match():
    add_user("Alice", "Smith", "1999-05-05")
    add_user("Alice", "Jones", "2001-07-07")

    results = search_users("Alice", "", "")
    assert len(results) == 2


def test_update_user():
    add_user("Jane", "Doe", "1995-02-02")
    users = fetch_all_users()

    user_id = users[0][0]
    update_user(user_id, "Janet", "Doe", "1995-02-02")

    updated = fetch_all_users()[0]
    assert updated[1] == "Janet"


def test_delete_user():
    add_user("Mark", "Twain", "1980-10-10")
    users = fetch_all_users()

    user_id = users[0][0]
    delete_user(user_id)

    rows = fetch_all_users()
    assert len(rows) == 0