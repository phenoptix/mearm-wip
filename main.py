def on_button_pressed_a():
    mearm.open_grip()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    mearm.close_grip()
input.on_button_pressed(Button.B, on_button_pressed_b)

def reset():
    mearm.move_to_centre(MearmServo.BASE)
    mearm.move_to_centre(MearmServo.RIGHT)
    mearm.move_to_centre(MearmServo.LEFT)
    mearm.move_to_centre(MearmServo.GRIP)
led.enable(False)
reset()

def on_forever():
    if mearm.joystick(Joystick.LEFT_JOY_X) < 0:
        mearm.move_by_angle(MearmServo.BASE, -1)
    elif mearm.joystick(Joystick.LEFT_JOY_X) > 0:
        mearm.move_by_angle(MearmServo.BASE, 1)
    if mearm.joystick(Joystick.LEFT_JOY_Y) < 0:
        mearm.move_by_angle(MearmServo.RIGHT, -1)
    elif mearm.joystick(Joystick.LEFT_JOY_Y) > 0:
        mearm.move_by_angle(MearmServo.RIGHT, 1)
    if mearm.joystick(Joystick.RIGHT_JOY_Y) < 0:
        mearm.move_by_angle(MearmServo.LEFT, -1)
    elif mearm.joystick(Joystick.RIGHT_JOY_Y) > 0:
        mearm.move_by_angle(MearmServo.LEFT, 1)
    if mearm.joystick(Joystick.RIGHT_JOY_X) < 0:
        mearm.move_by_angle(MearmServo.GRIP, -1)
    elif mearm.joystick(Joystick.RIGHT_JOY_X) > 0:
        mearm.move_by_angle(MearmServo.GRIP, 1)
basic.forever(on_forever)
