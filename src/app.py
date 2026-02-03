from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from datetime import datetime

APP_NAME = "DevSecOps Mini Frontend"
ENVIRONMENT = os.getenv("ENV", "dev")
VAULT_SECRET = os.getenv("DB_PASSWORD")

HTML_PAGE = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{APP_NAME}</title>
    <style>
        body {{
            font-family: Arial;
            background-color: #f2f4f8;
            text-align: center;
            padding-top: 60px;
        }}
        .box {{
            background: white;
            width: 420px;
            margin: auto;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #2c3e50; }}
        p {{ color: #34495e; }}
    </style>
</head>
<body>
    <div class="box">
        <h1>{APP_NAME}</h1>
        <p><b>Environment:</b> {ENVIRONMENT}</p>
        <p><b>Status:</b> Running ✅</p>
        <p><b>Vault Secret:</b> {"Fetched securely" if VAULT_SECRET else "Not provided"}</p>
        <p><b>Time:</b> {datetime.now()}</p>
    </div>
</body>
</html>
"""

class DevSecOpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode())

def run():
    server = HTTPServer(("0.0.0.0", 8080), DevSecOpsHandler)
    print(f"{APP_NAME} running on port 8080")
    server.serve_forever()

if __name__ == "__main__":
    run()
