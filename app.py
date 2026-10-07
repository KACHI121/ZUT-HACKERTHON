from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "campus-portal-secret"

DB = "students.db"


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        student_id = request.form["student_id"]
        password = request.form["password"]
        db = get_db()
        user = db.execute(
            "SELECT * FROM students WHERE student_id = ? AND password = ?",
            (student_id, password),
        ).fetchone()
        db.close()
        if user:
            session["student_id"] = user["student_id"]
            session["name"] = user["name"]
            return redirect(url_for("dashboard"))
        error = "Invalid student ID or password."
    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    if "student_id" not in session:
        return redirect(url_for("login"))
    return render_template(
        "dashboard.html", name=session["name"], student_id=session["student_id"]
    )


@app.route("/results")
def results():
    if "student_id" not in session:
        return redirect(url_for("login"))

    student_id = request.args.get("id") or session["student_id"]

    db = get_db()
    student = db.execute(
        "SELECT * FROM students WHERE student_id = ?", (student_id,)
    ).fetchone()
    db.close()

    if not student:
        return "Student not found.", 404

    return render_template("results.html", student=student)


@app.route("/wifi")
def wifi():
    return render_template("wifi.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
