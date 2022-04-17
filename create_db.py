import sqlite3

DATABASE = 'data.db'

con = sqlite3.connect(DATABASE)
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS status")
cur.execute("DROP TABLE IF EXISTS members")

cur.execute("PRAGMA foreign_keys=1")

cur.execute("""
    CREATE TABLE status (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        project TEXT NOT NULL,
        description TEXT
    )
""")

cur.execute("""
    CREATE TABLE members (
        id INTEGER PRIMARY KEY,
        status_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        is_leader INTEGER NOT NULL,
        FOREIGN KEY (status_id)
            REFERENCES status (id)
                ON UPDATE NO ACTION
                ON DELETE CASCADE
    )
""")

cur.execute("INSERT INTO status VALUES (1, '2022-04-16', 'project1', 'Lorem ipsum dolor sit amet,...')")
cur.execute("INSERT INTO status VALUES (2, '2022-04-17', 'project2', 'Lorem ipsum dolor sit amet,...')")

cur.execute("INSERT INTO members VALUES (NULL, 1, 'Mario', 1)")
cur.execute("INSERT INTO members VALUES (NULL, 2, 'Yoshi', 0)")
cur.execute("INSERT INTO members VALUES (NULL, 2, 'Luigi', 1)")

con.commit()
con.close()