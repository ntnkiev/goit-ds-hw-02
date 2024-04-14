import serial
import serial.tools.list_ports
# import rfranco
from serial.serialutil import SerialException


def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = {str(index + 1): port.device for index, port in enumerate(ports)}
    return available_ports


def main():
    while True:
        ports = list_serial_ports()
        if ports:
            print("Available serial ports:")
            for index, port in ports.items():
                print(f"{index}: {port}")
        else:
            print("Serial port not found.")

        user_input = input("Enter port number or press 'r' to refresh or 'q' to exit: ")
        if user_input == "r":
            pass
        elif user_input == "q":
            exit()
        else:
            port = ports.get(user_input)
            if port:
                with serial.Serial(port, 9600, timeout=1) as ser:
                    print(f"Port {port} open.")
                    while True:
                        data = ser.read()
                        if data == b'\x16\x05':
                            ser.write(b'\x11\x1B\x53\x1A\x03\x36\x0A')
                        elif data == b'\x16\x1B\x53\x30\x31\x30\x31\x30\x31\x30\x31\x6C\x47\x53\x20\x20\x20\x20\x20\x0A':
                            ser.write(
                                b"------------------------"b"\x0A\x1B"b"K!.MERKUR GAMING      17.00"b"\x0A\x1B"b"K"
                                b"'.EXCLUSIVA BONOS"
                                b"CF1  ES.           CF12 6.58 RC2"b"\x0A\x1B"b"K#.SALA NO.    :   00000000"b"\x0A\x1B"b"K$.MAQUINA NO."
                                b":   30100945.SERIE NO.   : 6130100945.REGION  "
                                b"Murcia_Excl_2015.------------------------.ETERNO DATOS:           .       "
                                b"06.03.24    17:17.       31.05.18    22:14.ULTIMA RECAUDACION:     "b"\x0A\x1B"b"K'."
                                b" 28.09.23    06:52.------------------------.TOTAL MONEDAS:          "b"\x0A\x1B"b"K"
                                b".. <"
                                b"EU >         33623.10.TOTAL BILLETES:         "b"\x0A\x1B"b"Kf. < EU >        "
                                b"101680.00.MONEDAS INTRODUCIDAS:   "b"\x0A\x1B"b"K.. < EU >        "
                                b"135303.10.------------------------.TOTAL MONEDAS:          "b"\x0A\x1B"b"K.. < EUR >"
                                b"  44901.00.TOTAL BILLETTES:        "b"\x0A\x1B"b"Kf. < EUR >            "
                                b"0.00.TOTAL CANCEL"
                                b"CREDIT:    "b"\x0A\x1B"b"K.. < EUR >        54584.90.MONEDAS PAGADAS:        "b"\x0A\x1B"b"K.. < EU >"
                                b"        99485.90.------------------------.BOLSA PREMIOS:          "b"\x0A\x1B"b"K|. "
                                b"< EUR"
                                b">            0.00.------------------------.PARTIDAS JUGADAS:       "b"\x0A\x1B"b"Kg."
                                b"            960607.TOTAL APOSTADO:         . < EUR >       192121.40.TOTAL "
                                b"PREMIOS:          . < EUR >       156304.00.------------------------.TOTAL "
                                b"RELLENADO:        "b"\x0A\x1B"b"K.. < EUR >         "
                                b"2373.00.------------------------.VJP"
                                b"COUNT:        881825..                       ..DATA NOT CLEARED..     .ENDE   "
                                b" NL.......")
                        else:
                            pass
                        # rfranco.rf_poll(ser)
                        # ser.close()
            else:
                print("Illegal port number.")
        # data = ser.readline()


if __name__ == '__main__':
    main()
