import unittest


class Machine:
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def switch_on(self):
        return f"{self.serial_number} start work"

class Transport(Machine):
    def __init__(self, serial_number):
        super().__init__(serial_number)

    def increase_speed(self):
        return f"{self.serial_number} speed up"

class Ground_Transport(Transport):
    def __init__(self, serial_number):
        super().__init__(serial_number)

    def decrease_speed(self):
        return f"{self.serial_number} slowing down"

class Automobile(Ground_Transport):
    def __init__(self, VIN):
        super().__init__(VIN)

class VAZ_2109(Automobile):
    def __init__(self, VIN):
        super().__init__(VIN)

    def horn(self):
        return f"{self.serial_number} makes beep-beep"


class Air_Transport(Transport):
    def __init__(self, serial_number):
        super().__init__(serial_number)

    def increase_height(self):
        return f"{self.serial_number} height up"

class Plane(Air_Transport):
    def __init__(self, serial_number):
        super().__init__(serial_number)

    def fly_up(self):
        speed_message = super().increase_speed()
        height_message = super().increase_height()
        return f"{speed_message} and {height_message}"


class TestMachineHeirs(unittest.TestCase):
    def test_VAZ(self):
        car = VAZ_2109("RTY654")
        self.assertEqual(car.switch_on(), "RTY654 start work")
        self.assertEqual(car.increase_speed(), "RTY654 speed up")
        self.assertEqual(car.decrease_speed(), "RTY654 slowing down")
        self.assertEqual(car.horn(), "RTY654 makes beep-beep")

    def test_Paragliding(self):
        plane = Plane("WASD")
        self.assertEqual(plane.switch_on(), "WASD start work")
        self.assertEqual(plane.fly_up(), "WASD speed up and WASD height up")
        self.assertEqual(plane.increase_speed(), "WASD speed up")
        self.assertEqual(plane.increase_height(), "WASD height up")
        
 

if __name__ == "__main__":
    unittest.main()
