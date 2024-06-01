import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for port in ports:
    portList.append(str(port))
    print(port)

choose = input("Seleziona una porta COM:")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(choose)):
        portVar = "COM" + str(choose)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'))