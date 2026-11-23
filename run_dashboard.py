"""
Python Launcher for Digital Payment Statistical Analysis Dashboard
Probability & Statistics Course Project
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    os.chdir(DIRECTORY)
    url = f"http://localhost:{PORT}/dashboard.html"
    print("=" * 60)
    print("📊 STUDENT DIGITAL PAYMENT HABITS - RESEARCH DASHBOARD")
    print(f"🚀 Serving locally at: {url}")
    print("💡 Opening in your default web browser...")
    print("Press Ctrl + C in this terminal to stop the server.")
    print("=" * 60)

    # Automatically open browser
    webbrowser.open(url)

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
