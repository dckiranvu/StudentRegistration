from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    usn = request.form["usn"]
    dept = request.form["dept"]

    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students(name, usn, dept)
        VALUES (?, ?, ?)
        """,
        (name, usn, dept)
    )

    conn.commit()
    conn.close()

    return f"""
    <h2>Student Registered Successfully</h2>

    Name : {name}<br>
    USN : {usn}<br>
    Department : {dept}<br><br>

    <a href="/">Register Another Student</a>
    """


if __name__ == "__main__":
    app.run(debug=True)