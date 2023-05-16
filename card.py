from smartcard.System import readers
from smartcard.util import toHexString

if __name__ == '__main__':
    r = readers()
    print(r)

    connection = r[0].createConnection()
    connection.connect()

    SELECT = [0x00, 0xA4, 0x04, 0x00, 0x08, 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x00]
    SEND = [0x00, 0x00, 0x00, 0x00]
    data, sw1, sw2 = connection.transmit(SELECT)
    print(toHexString(data))

    data, sw1, sw2 = connection.transmit(SEND)
    print(toHexString(data))