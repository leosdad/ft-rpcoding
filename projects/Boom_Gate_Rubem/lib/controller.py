import fischertechnik.factories as txt_factory  # type: ignore

txt_factory.init()
txt_factory.init_input_factory()
txt_factory.init_output_factory()
txt_factory.init_motor_factory()

TXT_M = txt_factory.controller_factory.create_graphical_controller()
home_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 1)
garage_button = txt_factory.input_factory.create_mini_switch(TXT_M, 2)
photo_transistor = txt_factory.input_factory.create_photo_transistor(TXT_M, 3)
gate_motor = txt_factory.motor_factory.create_encodermotor(TXT_M, 1)
green_led = txt_factory.output_factory.create_led(TXT_M, 3)
red_led = txt_factory.output_factory.create_led(TXT_M, 4)
gate_led = txt_factory.output_factory.create_led(TXT_M, 7)

txt_factory.initialized()
