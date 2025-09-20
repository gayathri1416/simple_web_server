# EX01 Developing a Simple Webserver

# Date:18.09.2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = '''
<html>
<head>
  <title>TCP/IP Protocol Suite</title>
</head>
<body style="background-color: rgba(20, 243, 180, 0.19);">
  <h1 align="center">TCP/IP Protocol Suite</h1>
  
  <ol>
    <li style="color: rgb(0, 0, 18); font-weight: bold;font-size: large;">Application Layer
      <ul style="color:rgb(6, 157, 162)">
        <li>HTTP (HyperText Transfer Protocol)</li>
        <li>HTTPS (HTTP Secure)</li>
        <li>FTP (File Transfer Protocol)</li>
        <li>SMTP (Simple Mail Transfer Protocol)</li>
        <li>POP3 / IMAP</li>
        <li>DNS (Domain Name System)</li>
        <li>DHCP (Dynamic Host Configuration Protocol)</li>
        <li>SSH (Secure Shell)</li>
        <li>Telnet</li>
        <li>SNMP (Simple Network Management Protocol)</li>
      </ul>
    </li>

    <li style="color: rgb(0, 0, 21); font-weight: bold;font-size: large">Transport Layer
      <ul style="color:rgb(5, 152, 157)">
        <li>TCP (Transmission Control Protocol)</li>
        <li>UDP (User Datagram Protocol)</li>
      </ul>
    </li>

    <li style="color: rgb(0, 0, 6); font-weight: bold;font-size: large" >Internet Layer
      <ul style="color:rgb(6, 153, 158)">
        <li>IP (IPv4 / IPv6)</li>
        <li>ICMP (Internet Control Message Protocol)</li>
        <li>IGMP (Internet Group Management Protocol)</li>
        <li>ARP (Address Resolution Protocol)</li>
      </ul>
    </li>

    <li style="color: rgb(0, 0, 10); font-weight: bold;font-size: large">Network Access / Link Layer
      <ul style="color:rgb(7, 138, 142)">
        <li>Ethernet</li>
        <li>PPP (Point-to-Point Protocol)</li>
        <li>Wi-Fi (IEEE 802.11)</li>
        <li>Frame Relay</li>
        <li>Token Ring</li>
      </ul>
    </li>
  </ol>
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
```
# OUTPUT:
![alt text](<Screenshot 2025-09-18 133554.png>)

![alt text](<Screenshot 2025-09-18 133626.png>)



# RESULT:
The program for implementing simple webserver is executed successfully.
