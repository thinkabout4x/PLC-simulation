class PLC:
    def __init__(self, target_pressure):
        self.target_pressure = target_pressure
        self.pressure_sensor = Pressure_sensor()
        self.open_sensor = Feedback_sensor(True)
        self.close_sensor = Feedback_sensor(False)

        self.analog_signal_pressure = None
        self.digital_signal_opened = None
        self.digital_signal_closed = None

    def read_input(self, current_pressure, solenoid_position):
        self.analog_signal_pressure = self.pressure_sensor.get_state(current_pressure)
        self.digital_signal_opened = self.open_sensor.get_state(solenoid_position)
        self.digital_signal_closed = self.close_sensor.get_state(solenoid_position)

    def get_state(self, current_pressure, solenoid_position):
        self.read_input(current_pressure,solenoid_position)
        print("Target pressure: ",self.target_pressure, " MPa")
        print("Pressure sensor: ",self.analog_signal_pressure, " V")
        print("Feedback sensor is_opened: ",self.digital_signal_opened, " V")
        print("Feedback sensor is_closed: ",self.digital_signal_closed, " V")

        target_pressure_volts = 4*self.target_pressure+1

        if target_pressure_volts >= self.analog_signal_pressure:
            print("Pressure in the system is ok to move the gripper")
        else:
            print("Pressure in the system is not ok to move the gripper")
        

class Pressure_sensor:
    def __init__(self):
        self.output_voltage = 1
    def measurement(self, pressure):
        self.output_voltage = 4*pressure+1
    def get_state(self, pressure):
        self.measurement(pressure)
        return self.output_voltage

class Feedback_sensor:
    def __init__(self, is_controlling_open_position):
        self.output_voltage = None
        self.location = is_controlling_open_position
    def measurement(self, solenoid):
        if self.location:
            if solenoid:
                self.output_voltage = 24.0
            else:
                self.output_voltage = 0.0
        else:
            if solenoid:
                self.output_voltage = 0.0
            else:
                self.output_voltage = 24.0
                
    def get_state(self, solenoid):
        self.measurement(solenoid)
        return self.output_voltage
