import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract query parameters
        from urllib.parse import parse_qs, urlparse
        query_params = parse_qs(urlparse(self.path).query)
        
        # Example student marks dictionary
        student_marks = {
            "Alice": 10,
            "Bob": 20,
            "Charlie": 30
        }
        
        # Get names from the request
        names = query_params.get("name", [])
        marks = [student_marks.get(name, 0) for name in names]

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # ✅ Enable CORS
        self.end_headers()

        # Return the marks in JSON format
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode(
