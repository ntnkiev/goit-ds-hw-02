import time

KEY = "RF\r\n".encode()  # default password
CLAVE = "clave\r\n".encode()  # password request
METERS = "contadores\r\n"  # all meters request
STATE = "estado\r\n".encode()  # state request
DATE_TIME = "fecha\r\n".encode()  # date and time
KEY_RESET = "genclave\r\n".encode()
ID = "id\r\n".encode()
HALL_NAME = "modlocal\r\n".encode()
SLOT_NUMBER = "modnumero\r\n".encode()
BET_WIN_GAME = "totales\r\n".encode()
VERSION = "version\r\n".encode()


def rf_poll(ser):
    while True:
        ser.write(CLAVE)
        data = ser.readline().decode('utf-8').strip()
        if data != "Clave:":
            time.sleep(5)
        else:
            ser.write(KEY)
