import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for port in ports:
    portList.append(str(port))
    print(port)

