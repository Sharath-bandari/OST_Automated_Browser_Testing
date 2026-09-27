from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# -------------------------------
# Create Database and Table
# -------------------------------
def create_database():

    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# Login Page
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Simple login credentials
        if username == "admin" and password == "admin123":

            return redirect("/students")

        else:

            return """
            <h1>Login Failed</h1>
            <p>Invalid username or password</p>
            <a href="/">Go Back</a>
            """

    return render_template("login.html")


# -------------------------------
# Student Management Page
# -------------------------------
@app.route("/students")
def students():

    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "students.html",
        students=students
    )


# -------------------------------
# Add Student
# -------------------------------
@app.route("/add_student", methods=["POST"])
def add_student():

    name = request.form["name"]
    email = request.form["email"]

    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()

    conn.close()

    return redirect("/students")


# -------------------------------
# Run Application
# -------------------------------
if __name__ == "__main__":

    create_database()

    app.run(debug=True)