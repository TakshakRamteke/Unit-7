from machine import Pin
from u7 import U7


led = Pin(2,Pin.OUT)

app = U7
app.run(app.render())
