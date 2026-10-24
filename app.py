from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from html import escape
import os

PORT = int(os.environ.get("PORT", "10000"))


class WelcomeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b"ok"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        message = escape(os.environ.get(
            "WELCOME_MESSAGE", "Hi, welcome to the Computing Systems Lab!"
        ))
        version = escape(os.environ.get("APP_VERSION", "v1"))
        requested_path = escape(self.path)

        page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Docker Welcome Lab</title>
  <style>
    body {{ font-family: system-ui, sans-serif; background: #eef5ff; color: #193354; margin: 0; padding: 8vh 5vw; }}
    main {{ max-width: 680px; margin: auto; background: white; padding: 28px; border-radius: 18px; box-shadow: 0 8px 30px #19335418; }}
    h1 {{ color: #1264c0; line-height: 1.2; }}
    .tag {{ display: inline-block; background: #e6f2ff; padding: 6px 10px; border-radius: 999px; font-size: .9rem; }}
    code {{ background: #f1f4f8; padding: 3px 6px; border-radius: 5px; }}
  </style>
</head>
<body>
  <main>
    <span class="tag">Live cloud container demo</span>
    <h1>{message}</h1>
    <p>This page is being served by a web application packaged as a Docker image.</p>
    <p><strong>Application version:</strong> {version}</p>
    <p><strong>Requested path:</strong> <code>{requested_path}</code></p>
    <p>Ask the instructor to deploy a new version, then refresh this same address.</p>
  </main>
</body>
</html>"""

        body = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        # Keep request logs readable in Render's deployment logs.
        print(f"{self.address_string()} - {format_string % args}")


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", PORT), WelcomeHandler)
    print(f"Welcome demo listening on 0.0.0.0:{PORT}")
    server.serve_forever()
