import sqlite3

conn = sqlite3.connect("students.db")
c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        fees_paid INTEGER NOT NULL,
        fees_required INTEGER NOT NULL
    )
    """
)

students = [
    ("2024001", "Angela Nyirenda", "12345678", 100, 100),
    ("2024002", "James Phiri", "2024002", 60, 100),
    ("2024003", "Grace Mwansa", "password", 100, 100),
    ("2024004", "Peter Zulu", "12345678", 0, 100),
]

c.executemany(
    """INSERT OR REPLACE INTO students
       (student_id, name, password, fees_paid, fees_required)
       VALUES (?, ?, ?, ?, ?)""",
    students,
)

conn.commit()
conn.close()
print("students.db seeded with starter data.")
