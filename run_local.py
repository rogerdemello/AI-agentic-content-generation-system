from http.server import HTTPServer
from api.generate import handler

def main():
    port = 8000
    server = HTTPServer(('0.0.0.0', port), handler)
    print(f"Local server running: http://localhost:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.server_close()

if __name__ == '__main__':
    main()
