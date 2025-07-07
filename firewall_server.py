# firewall_server.py

from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

# Define malicious indicators from headers
BLOCKED_HEADERS = {
    "suffix": "%>//",
    "c1": "Runtime",
    "c2": "<%",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define the targeted malicious path
BLOCKED_PATH = "/tomcatwar.jsp"


def is_malicious_request(path, headers):
    """
    Detect if the incoming request matches known RCE attack indicators.
    """
    if path == BLOCKED_PATH:
        # Check each malicious header
        for key, bad_value in BLOCKED_HEADERS.items():
            if key in headers and headers[key] == bad_value:
                print(f"[!] Blocked due to malicious header: {key}={bad_value}")
                return True
        # Even without headers, restrict access to the endpoint
        print("[!] Blocked due to access to /tomcatwar.jsp")
        return True
    return False


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if is_malicious_request(self.path, self.headers):
            self.send_response(403)  # Forbidden
            self.end_headers()
            self.wfile.write(b'{"error": "Forbidden"}')
            print(f"Blocked GET request to {self.path}")
        else:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "GET request allowed"}')
            print(f"Allowed GET request to {self.path}")

    def do_POST(self):
        if is_malicious_request(self.path, self.headers):
            self.send_response(403)  # Forbidden
            self.end_headers()
            self.wfile.write(b'{"error": "Forbidden"}')
            print(f"Blocked POST request to {self.path}")
        else:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "POST request allowed"}')
            print(f"Allowed POST request to {self.path}")


if __name__ == "__main__":
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print(f"[+] HTTP Web Server running on: {host}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)
