import network
import socket
import time
from machine import Pin

# ---------------------------
# Configuración WiFi
# ---------------------------
SSID = "TU_WIFI"
PASSWORD = "TU_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Conectando a WiFi...")
while not wlan.isconnected():
    time.sleep(1)
print("Conectado:", wlan.ifconfig())

# ---------------------------
# Configuración Motor y Pines
# ---------------------------
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

# Secuencia para paso completo (motor 28BYJ / M35SP)
secuencia = [
    [1,0,1,0],
    [0,1,1,0],
    [0,1,0,1],
    [1,0,0,1]
]

# Variables globales
direccion = 1   # 1 = CW, -1 = CCW
posicion_pasos = 0

# ---------------------------
# Funciones
# ---------------------------
def mover_motor(pasos):
    global posicion_pasos
    for i in range(pasos):
        idx = (i * direccion) % 4
        IN1.value(secuencia[idx][0])
        IN2.value(secuencia[idx][1])
        IN3.value(secuencia[idx][2])
        IN4.value(secuencia[idx][3])
        posicion_pasos = (posicion_pasos + direccion) % 48  # 48 pasos = 360°
        time.sleep(0.05)

def generar_html():
    angulo = posicion_pasos * 7.5
    html = f"""
    <html>
    <head>
      <title>Control Motor a Pasos</title>
      <style>
        body {{ font-family: Arial; text-align: center; }}
        button {{ padding: 15px; margin: 10px; font-size: 18px; }}
        #reloj {{ width: 300px; height: 300px; border: 2px solid black; border-radius: 50%; margin: auto; position: relative; }}
        #aguja {{
          width: 2px; height: 120px; background: red;
          position: absolute; top: 30px; left: 149px;
          transform: rotate({angulo}deg);
          transform-origin: bottom center;
        }}
      </style>
    </head>
    <body>
      <h1>Control de Motor M35SP7T</h1>
      <p>Pasos actuales: {posicion_pasos} / 48</p>
      <div id="reloj">
        <div id="aguja"></div>
      </div>
      <br>
      <a href="/cw"><button>Clockwise</button></a>
      <a href="/ccw"><button>Counter Clockwise</button></a>
      <a href="/start"><button>Start</button></a>
    </body>
    </html>
    """
    return html

# ---------------------------
# Servidor Web
# ---------------------------
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Servidor corriendo en http://", wlan.ifconfig()[0])

while True:
    cl, addr = s.accept()
    request = cl.recv(1024).decode()
    
    if "/cw" in request:
        direccion = 1
    elif "/ccw" in request:
        direccion = -1
    elif "/start" in request:
        mover_motor(5)  # mueve 5 pasos cada clic en Start
    
    response = generar_html()
    cl.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
    cl.send(response)
    cl.close()
