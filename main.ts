input.onButtonPressed(Button.A, function on_button_pressed_a() {
    mearm.openGrip()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    reset()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    mearm.closeGrip()
})
function reset() {
    mearm.moveToCentre(MearmServo.Base)
    mearm.moveToCentre(MearmServo.Right)
    mearm.moveToCentre(MearmServo.Left)
    mearm.moveToCentre(MearmServo.Grip)
}

led.enable(false)
reset()
basic.forever(function on_forever() {
    if (mearm.joystick(Joystick.LeftJoyX) < 0) {
        mearm.moveByAngle(MearmServo.Base, -1)
    } else if (mearm.joystick(Joystick.LeftJoyX) > 0) {
        mearm.moveByAngle(MearmServo.Base, 1)
    }
    
    if (mearm.joystick(Joystick.LeftJoyY) < 0) {
        mearm.moveByAngle(MearmServo.Right, -1)
    } else if (mearm.joystick(Joystick.LeftJoyY) > 0) {
        mearm.moveByAngle(MearmServo.Right, 1)
    }
    
    if (mearm.joystick(Joystick.RightJoyY) < 0) {
        mearm.moveByAngle(MearmServo.Left, -1)
    } else if (mearm.joystick(Joystick.RightJoyY) > 0) {
        mearm.moveByAngle(MearmServo.Left, 1)
    }
    
    if (mearm.joystick(Joystick.RightJoyX) < 0) {
        mearm.moveByAngle(MearmServo.Grip, -1)
    } else if (mearm.joystick(Joystick.RightJoyX) > 0) {
        mearm.moveByAngle(MearmServo.Grip, 1)
    }
    
})
