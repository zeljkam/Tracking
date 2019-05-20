from bluepy.btle import Scanner, DefaultDelegate

def device_description(value):
    print("  %s = %s" % (desc, value))
    data = value[0:32]  # uzmi samo prvih 16 bajtova iz Service data(DATA)
    data_value = ""
    for num in range(0, 16):
        data_value += value[
                      30 - num * 2: 32 - num * 2]  # zamijeni redoslijed svakog bajta, ispisuje bajt[30,32] zatim bajt [28,30] kako i pise u BTapi
    print("  data = %s" % (data))  # ispisuje prvih 16 bajtova iz Service data(DATA)
    print("  data_value = %s" % (data_value))  # ispisi pravilan redosljed kak i pise u BTapi



def node(value):
    operation_mode = bin(int(value[32]))
    print("\n  operation_mode = %s" % (operation_mode))  # ispisuje 4 bita binarno iz Service data(DATA)

    flags_uwb = bin(int(value[33]))
    print("  flags_uwb = %s" % (flags_uwb))  # ispisuje 4 bita binarno iz Service data(DATA)

    change_counter = int(value[34])
    print ("  Change counter changes each %d ms when a characteristic gets changed!" %change_counter)

    if operation_mode == "0b1000":
        print("  Uredaj je konfiguriran kao anchor!")
        #return anchor
    elif operation_mode == "0b1000":
        print("  Uredaj je konfiguriran kao tag!")
        #return tag

    if flags_uwb == "0b00":
        print("  UWB je off!\n")
    elif  flags_uwb == "0b01":
        print("  UWB je passive!\n")
    elif  flags_uwb == "0b10":
        print("  UWB je active! \n")


if __name__ == '__main__':
    print("Zeljka nema linux")
    print("test")
    scanner = Scanner() #pokreni skeniranje
    while True:
        print("Scanning...")
        devices = scanner.scan(1.0)
        print("DONE!")

        for dev in devices:
            print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
            for (adtype, desc, value) in dev.getScanData():
                if desc == ("128b Service Data"):
                   device_description(value)
                   node(value)





