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
<!doctype html>
<html>
<head>
  <title>TCP/IP Protocol Suite</title>
</head>
<body style="background-color: rgba(20, 243, 180, 0.19);">
  <h1 align="center">TCP/IP Protocol Suite</h1>
  
  <table border="1" align="center" cellpadding="10" cellspacing="0" style="border-collapse: collapse; font-size: 16px;">
    <tr style="background-color:rgb(6, 157, 162) ; color: white; font-weight: bold; text-align: center;">
      <th>Layer</th>
      <th>Protocols</th>
    </tr>

    <tr>
      <td style="font-weight:bold; color:rgb(0, 0, 18);">Application Layer</td>
      <td style="color:rgb(6, 157, 162);">
        HTTP, HTTPS, FTP, SMTP, POP3/IMAP, DNS, DHCP, SSH, Telnet, SNMP
      </td>
    </tr>

    <tr>
      <td style="font-weight:bold; color:rgb(0, 0, 21);">Transport Layer</td>
      <td style="color:rgb(5, 152, 157);">
        TCP, UDP
      </td>
    </tr>

    <tr>
      <td style="font-weight:bold; color:rgb(0, 0, 6);">Internet Layer</td>
      <td style="color:rgb(6, 153, 158);">
        IP (IPv4/IPv6), ICMP, IGMP, ARP
      </td>
    </tr>

    <tr>
      <td style="font-weight:bold; color:rgb(0, 0, 10);">Network Access / Link Layer</td>
      <td style="color:rgb(7, 138, 142);">
        Ethernet, PPP, Wi-Fi (IEEE 802.11), Frame Relay, Token Ring
      </td>
    </tr>
  </table>
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
![alt text](<Screenshot 2025-09-22 212530.png>)
![alt text](<Screenshot 2025-09-22 212428.png>)





# RESULT:
The program for implementing simple webserver is executed successfully.
