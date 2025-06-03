def on_received_string(receivedString):
    x = int(receivedString[0])
    y = int(receivedString[1])
    led.plot(x, y)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("42")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a_b():
        led.plot(4, 2)
input.on_button_pressed(Button.AB, on_button_pressed_a_b)

radio.set_group(16)

def on_forever():
    pass
basic.forever(on_forever)
