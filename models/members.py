import sqlite3

DATABASE = 'data.db'


class MemberModel():
    TABLE = 'members'

    def __init__(self, _id, status_id, name, id_leader):
        self.id = _id
        self.status_id = status_id
        self.name = name
        self.id_leader = id_leader

    def __str__(self):
        return f"id: {self.id}, status_id: {self.status_id}, name: {self.name}, id_leader: {self.id_leader}"

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

    @classmethod
    def find_by_status_id(cls, status_id):
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = f"SELECT * FROM {cls.TABLE} WHERE status_id = ?"
        rows = cur.execute(query, (status_id,)).fetchall()

        con.close()

        if rows:
            models = [cls(*row) for row in rows]
        else:
            models = []
            
        return models


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
            SET status_id = ?,
                name = ?,
                id_leader = ?
            WHERE id = ?
        """
        cur.execute(query, (self.status_id, self.name, self.id_leader, self.id))
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
        cur.execute(query, (self.status_id, self.name, self.id_leader))
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