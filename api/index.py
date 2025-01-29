import json
import urllib.parse
from http.server import BaseHTTPRequestHandler

# Simulated student marks dictionary
marks_dict = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40
}  # Extend this with 100 students' marks

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = urllib.parse.parse_qs(self.path[2:])  # Removing leading "/?"
        names = query.get("name", [])  # Get all "name" parameters

        # Fetch marks for requested names
        marks = [marks_dict.get(name, "Not Found") for name in names]

        # Enable CORS
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Enable CORS
        self.end_headers()

        # Return JSON response
        self.wfile.write(json.dumps({"marks": marks}).encode("utf-8"))
