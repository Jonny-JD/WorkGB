import json
import os
from datetime import datetime


class NoteManager:
    def __init__(self, file_name="notes.json"):
        self.file_name = file_name
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.notes = json.load(file)

    def save_notes(self):
        with open(self.file_name, "w") as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, title, body):
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "body": body,
            "timestamp": str(datetime.now())
        }
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note["id"] == note_id:
                note["title"] = title
                note["body"] = body
                note["timestamp"] = str(datetime.now())
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                self.save_notes()
                return True
        return False

    def list_notes(self):
        if self.notes:
            for note in self.notes:
                print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")
        else:
            print("No notes found.")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                return note
        return None

    def filter_notes_by_date(self, start_date, end_date):
        filtered_notes = [note for note in self.notes if start_date <= note["timestamp"] <= end_date]
        if filtered_notes:
            for note in filtered_notes:
                print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")
        else:
            print("No notes found in the specified date range.")
