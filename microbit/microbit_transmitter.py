radio.set_group(100)

def on_forever():
    radio.send_number(input.acceleration(Dimension.STRENGTH))
    basic.pause(100)
basic.forever(on_forever)

# BLOCK CODE LINK -> https://makecode.microbit.org/S15428-08207-33906-59529
