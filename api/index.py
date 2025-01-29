import json
from http.server import BaseHTTPRequestHandler
import os

# Example dictionary with student marks
student_marks = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    # Add other student marks here
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow any origin
        self.send_header('Access-Control-Allow-Methods', 'GET')  # Allow only GET requests
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Allow Content-Type header
        
        # Parse query parameters
        query = self.parse_query()
        names = query.get('name', [])
        
        marks = [student_marks.get(name, "Student not found") for name in names]
        
        # Prepare response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Return the marks as a JSON response
        self.wfile.write(json.dumps({"marks": marks}).encode('utf-8'))
    
    def parse_query(self):
        """Parse the query string into a dictionary."""
        query = {}
        if '?' in self.path:
            path, query_string = self.path.split('?', 1)
            for param in query_string.split('&'):
                key, value = param.split('=')
                if key in query:
                    query[key].append(value)
                else:
                    query[key] = [value]
        return query
