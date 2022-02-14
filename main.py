def on_button_pressed_a():
    music.play_melody("C5 B A G A B C5 C ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    music.play_melody("- - D F A C5 B A ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
""")

def on_forever():
    pass
basic.forever(on_forever)
