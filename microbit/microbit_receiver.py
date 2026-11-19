def on_received_number(receivedNumber):
    global strength
    strength = receivedNumber
    basic.pause(200)
radio.on_received_number(on_received_number)

strength = 0
radio.set_group(100)
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)

def on_forever():
    if strength > 1800:
        serial.write_line("A")
        basic.pause(2000)
basic.forever(on_forever)




# unsure on linearity of code but will investigate

# https://makecode.microbit.org/S66189-95708-82154-28113
