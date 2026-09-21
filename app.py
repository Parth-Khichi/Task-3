from flask import Flask, render_template, request
import bcrypt

from connect import conn

app = Flask(__name__)


# Show registration page
@app.route("/")
def home():
    return render_template("register.html")


# Handle registration
@app.route("/register", methods=["POST"])
def register():

    # Get data from the form
    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip()
    gender = request.form.get("gender")
    password = request.form.get("password", "")

    # Check username
    if not username:
        return "Username is required"

    # Check email
    if not email:
        return "Email is required"

    # Check gender
    if not gender:
        return "Please select a gender"

    # Check password
    if not password:
        return "Password is required"

    if len(password) < 6:
        return "Password must be at least 6 characters"

    # Hash the password before saving it
    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    # Convert hash to text for MySQL
    password_hash = password_hash.decode("utf-8")

    # Insert user into MySQL
    cursor = conn.cursor()

    query = """
        INSERT INTO users1
        (username, email, gender, password)
        VALUES (%s, %s, %s, %s)
    """

    values = (
        username,
        email,
        gender,
        password_hash
    )

    cursor.execute(query, values)

    # Save changes
    conn.commit()

    cursor.close()

    return "Registration successful!"


if __name__ == "__main__":
    app.run(debug=True)
