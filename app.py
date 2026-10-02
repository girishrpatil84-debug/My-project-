from flask import Flask, request
from datetime import datetime
import platform

app = Flask(__name__)

def render_dashboard(title, content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background-color: #121212;
                color: #e0e0e0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background: #1e1e1e;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.5);
                text-align: center;
                border: 1px solid #333;
                width: 320px;
                max-width: 90%;
            }}
            nav {{ margin-bottom: 20px; }}
            nav a {{
                color: #2196f3;
                text-decoration: none;
                margin: 0 10px;
                font-weight: bold;
            }}
            nav a:hover {{ text-decoration: underline; }}
            h1 {{ color: #4caf50; margin-bottom: 8px; }}
            input[type="text"] {{
                width: 80%;
                padding: 10px;
                margin: 15px 0;
                background: #252525;
                border: 1px solid #444;
                border-radius: 8px;
                color: #fff;
                font-size: 16px;
                text-align: center;
            }}
            button {{
                background: #4caf50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 8px;
                cursor: pointer;
                font-weight: bold;
            }}
            button:hover {{ background: #45a049; }}
            .reply {{ margin-top: 15px; font-weight: bold; color: #ff9800; font-size: 18px; }}
        </style>
    </head>
    <body>
        <nav>
            <a href="/">🏠 Home</a> | <a href="/greet">👋 Greet</a> | <a href="/about">ℹ️ About</a>
        </nav>
        <div class="card">
            {content}
        </div>
    </body>
    </html>
    """

@app.route("/")
def home():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    body = f"""
        <h1>Home Base</h1>
        <p>Your local Python server is running beautifully!</p>
        <div style="font-size: 24px; font-weight: bold; color: #2196f3; margin: 15px 0;">{current_time}</div>
    """
    return render_dashboard("Home - Dashboard", body)

@app.route("/greet", methods=["GET", "POST"])
def greet():
    reply_message = ""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if username:
            reply_message = f"<div class='reply'>Hello, {username}! Welcome to your server. ✨</div>"
        else:
            reply_message = "<div class='reply' style='color: #f44336;'>Please type a name! ❌</div>"
            
    body = f"""
        <h1>Interactive Greet</h1>
        <p>Type your name below to interact with the Python backend:</p>
        <form method="POST" action="/greet">
            <input type="text" name="username" placeholder="Enter your name" autocomplete="off">
            <br>
            <button type="submit">Submit to Python</button>
        </form>
        {reply_message}
    """
    return render_dashboard("Greet - Dashboard", body)

@app.route("/about")
def about():
    system_info = f"OS: {platform.system()} | Machine: {platform.machine()}"
    body = f"""
        <h1>About System</h1>
        <div style="color: #aaa; text-align: left; font-size: 14px; background: #252525; padding: 10px; border-radius: 8px; margin-top: 10px;">
            <strong>Specs:</strong><br>
            • Platform: Ubuntu Linux<br>
            • {system_info}<br>
            • Backend: Python / Flask
        </div>
    """
    return render_dashboard("About - Dashboard", body)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
