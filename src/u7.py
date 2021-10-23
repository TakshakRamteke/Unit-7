try :
    import usocket as socket
except :
    import socket

class U7():

    def __init__(self):
        pass

    def render():
        with open("/examples/test.html", "r", encoding='utf-8') as file:
            html = file.read()
        file.close()
        return html
    
    def run(html):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('', 80))
        server.listen(5)
        conn, addr = server.accept()
        print('Received HTTP GET connection request from %s' % str(addr))
        response = html
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.sendall(response)
        conn.close()


