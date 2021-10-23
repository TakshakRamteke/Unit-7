try :
    import usocket as socket
except :
    import socket

class U7():

    def __init__(self, ssid, password):

        self.ssid = ssid
        self.password = password

    def html_to_string(file_location):
        with open(file_location, "r", encoding='utf-8') as f:
            text= f.read()
        f.close()
        return text