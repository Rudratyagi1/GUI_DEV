import json
import re

class Database:
    def __init__(self, db_file='db.json'):
        self.db_file = db_file

    def _load_database(self):
        """Loads the database from a JSON file, handling missing or corrupted files gracefully."""
        try:
            with open(self.db_file, 'r') as rf:
                return json.load(rf)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_database(self, database):
        """Saves the database back to the JSON file."""
        with open(self.db_file, 'w') as wf:
            json.dump(database, wf, indent=4)

    def _validate_email(self, email):
        """Validates email using a regular expression pattern."""
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email)

    def add_data(self, name, email, password):
        """Adds a new user to the database if the email doesn't already exist."""
        if not self._validate_email(email):
            return "Invalid email format"  # Error handling for invalid email format

        database = self._load_database()

        if email in database:
            return 0  # Email already exists
        else:
            database[email] = [name, password]
            self._save_database(database)
            return 1  # Successfully added

    def search(self, email, password):
        """Searches for a user by email and password, returning success or failure."""
        database = self._load_database()

        if email in database:
            if database[email][1] == password:
                return 1  # Login successful
            else:
                return 0  # Incorrect password
        else:
            return 0  # Email not found