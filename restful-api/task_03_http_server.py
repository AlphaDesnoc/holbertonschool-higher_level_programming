#!/usr/bin/python3
"""
This module implements a simple HTTP server with multiple endpoints.
"""

import http.server
import json

# Define the port on which the server will listen
PORT = 8000

# Define the base request handler
server = http.server.BaseHTTPRequestHandler


class Server(server):
    """
    Custom HTTP server class that handles GET
        requests for predefined endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests and responds based on the requested endpoint.
        """
        if self.path == '/':
            # Respond to the root endpoint with a welcome message
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # Respond to /data with a JSON object
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/info":
            # Respond to /info with API details
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        elif self.path == "/status":
            # Respond to /status with an OK message
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Respond with 404 for unknown endpoints
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    # Initialize and start the HTTP server
    with http.server.HTTPServer(("", PORT), Server) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
