import sqlite3
import random

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS information (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                text TEXT NOT NULL
            )
        """)

    def add_info(self, category, text):
        self.cursor.execute(
            "INSERT INTO information (category, text) VALUES (?, ?)",
            (category, text)
        )
        self.connection.commit()

    def get_random_info(self, category):
        self.cursor.execute(
            "SELECT text FROM information WHERE category = ?",
            (category,)
        )

        results = self.cursor.fetchall()

        if results:
            return random.choice(results)[0]

        return "No information found"