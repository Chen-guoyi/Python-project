"""智能家居系统"""
class Device:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def turn_on(self):
        print("The light is bright now.")

    def turn_off(self):
        print("It turns black.")


class Light(Device):
    def __init__(self, name, room):
        super().__init__(name, room)
        self.brightness = 0

    def adjust_bright(self, level):
        self.brightness = level

class AirCondition(Device):
    def __init__(self, name, room):
        super().__init__(name, room)
        self.temp = 26

    def turn_on(self):
        print(f"The aircondintion is {self.temp} ℃ now.")

    def set_temp(self, temp):
        self.temp = temp


class SmartHome:
    def __init__(self):
        self.light = Light("客厅灯", "客厅")
        self.aircondition = AirCondition("主卧空调", "主卧")

    def home_status(self):
        print("现在家里的设备状态是：")


smarthome = SmartHome()
smarthome.light.turn_on()
smarthome.light.adjust_bright()