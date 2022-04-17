import sqlite3

DATABASE = 'data.db'


class StatusModel():
    TABLE = 'status'

    def __init__(self, _id, date, project, description):
        self.id = _id
        self.date = date
        self.project = project
        self.description = description

    def __str__(self):
        return f"id: {self.id}, date: {self.date}, project: {self.project}, description: {self.description}"

    @classmethod
    def find_by_id(cls, _id):
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = f"SELECT * FROM {cls.TABLE} WHERE id = ?"
        result = cur.execute(query, (_id,)).fetchone()

        con.close()

        if result:
            obj = cls(*result)
        else:
            obj = None

        return obj

    def save(self):
        if self.find_by_id(self.id):
            self.update()
        else:
            self.insert()

    def update(self):
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=1")

        query = f"""
            UPDATE {self.TABLE}
            SET date = ?,
                project = ?,
                description = ?
            WHERE id = ?
        """
        cur.execute(query, (self.date, self.project, self.description, self.id))
        con.commit()
        con.close()

    def insert(self):
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=1")

        query = f"""
            INSERT INTO {self.TABLE}
            VALUES (
                NULL,
                ?,
                ?,
                ?
            )
        """
        cur.execute(query, (self.date, self.project, self.description))
        self.id = cur.lastrowid
        con.commit()
        con.close()

    def delete(self):
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys=1")

        query = f"DELETE FROM {self.TABLE} WHERE id = ?"
        cur.execute(query, (self.id,))

        con.commit()
        con.close()     