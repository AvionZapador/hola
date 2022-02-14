input.onButtonPressed(Button.A, function () {
    music.playMelody("C5 B A G A B C5 C ", 120)
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("- - D F A C5 B A ", 120)
})
basic.showLeds(`
    . . . . .
    . . # . .
    . # . # .
    . . # . .
    . . . . .
    `)
basic.forever(function () {
	
})
