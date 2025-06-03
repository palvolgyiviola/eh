radio.onReceivedString(function on_received_string(receivedString: string) {
    let x = parseInt(receivedString[0])
    let y = parseInt(receivedString[1])
    led.plot(x, y)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("42")
})
input.onButtonPressed(Button.AB, function on_button_pressed_a_b() {
    led.plot(4, 2)
})
radio.setGroup(16)
basic.forever(function on_forever() {
    
})
