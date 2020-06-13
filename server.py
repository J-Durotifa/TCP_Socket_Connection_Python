import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(("", port))
print("Socket bound to %s" % port)

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    data = bytes("Thanks for connecting", "utf-8")
    c.send(data)
    print("Data sent")
    # if key == ord('q'):
    #     break
    if KeyboardInterrupt:
        c.close()
        break
