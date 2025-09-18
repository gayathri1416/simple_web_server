from http.server import HTTPServer, BaseHTTPRequestHandler
content = '''
<html>
<head><title>Laptop Configuration</title></head>
<body>
    <center style="font-size: x-large;" >
        <h1>Laptop Configuration Details</h1>
        <p><b>Edition:</b> Windows 11 Home Single Language
        <p><b>Version:</b> 24H2
        <p><b>Processor:</b> 12th Gen Intel(R) Core(TM) i5-12450HX (2.40 GHz) 
        <p><b>Installed RAM:</b> 16.0 GB (15.7 GB usable) 
        <p><b>System type:</b> 64-bit operating system, x64-based processor
</body>
</html>
'''

class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('', 8000)
httpd = HTTPServer(server_address, Myserver)
httpd.serve_forever()