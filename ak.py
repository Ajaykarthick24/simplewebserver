from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>

        </title>
    </head>
    <body>
        <h1>Device specification(Ajay karthick M)</h1>

        <table border="10" width="800" height="500" cellpadding="50" bgcolor="lightblue" align="center">
            <tr>
                <th bgcolor="blue">S.no</th>
                <th bgcolor="Yellow">Device specification</th>
                <th bgcolor="cyan">Type</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Device name</td>
                <td>Ajay laptop</td>
            </tr>
            <tr>
                <td>2</td>
                <td>processor</td>
                <td>13th Gen Intel(R) Core(TM) i7-13620H (2.40 GHz)</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed ram</td>
                <td>16gb ram</td>
            </tr>
            <tr>
                <td>4</td>
                <td>System type</td>
                <td>64-bit operating system, x64-based processor</td>
            </tr>
            <tr>    
                <td>5</td>
                <td>Pen and touch</td>
                <td>No pen or touch input is available for this display</td>   
        </table>
    
    </body>

</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()