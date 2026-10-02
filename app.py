from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Termux Server</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background-color: #121212;
                color: #e0e0e0;
                display: flex;
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
                max-width: 90%;
            }}
            h1 {{ color: #4caf50; margin-bottom: 8px; }}
            .time {{ font-size: 24px; font-weight: bold; color: #2196f3; margin: 15px 0; }}
            .date {{ color: #888; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Termux Dashboard</h1>
            <p>Your local Python server is running beautifully!</p>
            <div class="time">{current_time}</div>
            <div class="date">{current_date}</div>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
