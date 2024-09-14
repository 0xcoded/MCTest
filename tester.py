import socket

IP = input("IP: ")

Port = input("Puerto (25565): ")
if Port != "":
        Port = int(Port)
else:
        Port = 25565

try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                #s.connect(("na18.holy.gg", 26247))
                #s.connect((str(IP), 26247))
                s.connect((str(IP), Port))

                print("Servidor está ABIERTO (" + IP + ":" + str(Port) + ")")
except:
        print("Servidor NO DISPONIBLE (" + IP + ":" + str(Port) + ")")
