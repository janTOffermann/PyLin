# Py Lin

Py Lin provides the ability to control a Lin Engineering stepper motor driver using simple commands. 
Typical usage often looks like this:

    #!/usr/bin/env python

    from pylin import driver

    my_driver = driver.driver(usb_port_name,1)
    my_driver.Step(1000)
    print("Your stepper motor with controller address 1 should be stepping forward 1000 microsteps.")

