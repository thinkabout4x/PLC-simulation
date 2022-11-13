from plc_simulation import *


target_pressure = 0.4
plc = PLC(target_pressure)


if __name__ == "__main__":
    while True:
        while True:
            pressure_in_system = input("Enter the system pressure from 0 to 0.7 Mpa: ")
            try:
                pressure_in_system = float(pressure_in_system)
                if pressure_in_system < 0. or pressure_in_system > 0.7:
                    raise  Exception
                break
            except ValueError:
                continue
            except Exception:
                continue

        while True:
            solenoid_position = input("Enter the solenoid position 0-closed, 1- opened: ")
            try:
                solenoid_position = int(solenoid_position)
                if solenoid_position != 0 and solenoid_position != 1:
                    raise  Exception
                break
            except ValueError:
                continue
            except Exception:
                continue

        plc.get_state(pressure_in_system, solenoid_position)

     