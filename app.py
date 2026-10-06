from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

USERNAME = "radha"
PASSWORD = "143"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Website</title>
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #111827, #4c1d95, #0f766e);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .box {
            width: 90%;
            max-width: 420px;
            padding: 30px;
            border-radius: 24px;
            background: rgba(255,255,255,0.12);
            backdrop-filter: blur(15px);
            box-shadow: 0 10px 40px rgba(0,0,0,.35);
            text-align: center;
        }
        h1 { margin-bottom: 25px; }
        input {
            width: 100%;
            padding: 14px;
            margin: 8px 0;
            border: 0;
            border-radius: 12px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 14px;
            margin-top: 12px;
            border: 0;
            border-radius: 12px;
            background: #fff;
            color: #111827;
            font-weight: bold;
            font-size: 16px;
        }
        .menu {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
        .card {
            padding: 25px 10px;
            border-radius: 18px;
            background: rgba(255,255,255,.15);
        }
        a {
            color: white;
            text-decoration: none;
        }
        .error { color: #ffb4b4; }
    </style>
</head>
<body>
    <div class="box">
        {% if page == "login" %}
            <h1>🔐 My Website</h1>

            {% if error %}
                <p class="error">{{ error }}</p>
            {% endif %}

            <form method="POST">
                <input name="username" placeholder="Username" required>
                <input name="password" type="password" placeholder="Password" required>
                <button type="submit">LOGIN</button>
            </form>

        {% else %}
            <h1>✨ Welcome</h1>
            <p>Choose what you want to open</p>

            <div class="menu">
                <a href="#"><div class="card">🎵<br>Music</div></a>
                <a href="#"><div class="card">📁<br>Files</div></a>
                <a href="#"><div class="card">🖼️<br>Photos</div></a>
                <a href="#"><div class="card">📄<br>Documents</div></a>
            </div>

            <form action="/logout" method="POST">
                <button type="submit">LOGOUT</button>
            </form>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if (request.form.get("username") == USERNAME and
                request.form.get("password") == PASSWORD):
            session["logged_in"] = True
            return redirect("/")

        return render_template_string(
            HTML, page="login", error="Invalid username or password"
        )

    if not session.get("logged_in"):
        return render_template_string(HTML, page="login", error=None)

    return render_template_string(HTML, page="home")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

