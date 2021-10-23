import network

ssid = "your ssid"                  
password = "your password"    

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

station.ifconfig()