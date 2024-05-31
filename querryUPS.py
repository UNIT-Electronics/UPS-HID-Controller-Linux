"""
Description: This script provides methods for controlling a UPS USB device on a Linux system.

Author: Adrian Rabadan Ortiz

Date Created: May 29, 2024

Date Modified: Month DD, Year

Version: 1.0

Dependencies: UPSManager
"""

from controlUPS import UPSManager
import json
import time

# Initialize UPSManager with UPS details
ups_manager = UPSManager("koblenz-7016", "admin", "admin_password")

def restartUPSServices(_print=0):
    """
    Restarts the UPS services (nut-server and nut-monitor).

    Args:
        _print (int, optional): If set to 1, prints the output of the command. Defaults to 0.
    """
    if _print == 1:
        print(ups_manager.restart_nut_services())
    else:
        ups_manager.restart_nut_services()

def readUPS():
    """
    Reads various metrics from the UPS and returns them as a JSON string.

    Returns:
        str: JSON string containing the UPS metrics.
    """
    # Create a structured data dictionary
    output_structure = {
        "BatL": ups_manager.get_battery_level() + '%',
        "Vbat": ups_manager.get_battery_voltage() + 'V',
        "Vin": ups_manager.get_input_voltage() + 'V',
        "Vout": ups_manager.get_output_voltage() + 'V',
        "Mode": ups_manager.get_ups_mode(),
        "Freq": ups_manager.get_frequency() + 'Hz'
    }

    # Replace \n with space in each value of the dictionary
    for key in output_structure:
        if isinstance(output_structure[key], str):
            output_structure[key] = output_structure[key].replace('\n', ' ').strip()

    json_output = json.dumps(output_structure, indent=4)

    return json_output

def restartDelay(_print=0):
    """
    Shuts down the UPS after a delay (see /etc/nut ups.conf [offdelay]) and restarts it after ups.delay.start

    Args:
        _print (int, optional): If set to 1, prints the output of the command. Defaults to 0.
    """
    if _print == 1:
        print("Shutting down UPS after [delayoff] seconds, please wait ...")
        print(ups_manager.shutdown_delay())
    else:
        ups_manager.shutdown_delay()

def powerOnLoad(_print=0):
    """
    Immediately turns on the load on the UPS.

    Args:
        _print (int, optional): If set to 1, prints the output of the command. Defaults to 0.
    """
    if _print == 1:
        print("Powering on the UPS...")
        print(ups_manager.power_on_load())
    else:
        ups_manager.power_on_load()

def powerOffLoad(_print=0):
    """
    Immediately turns off the load on the UPS.

    Args:
        _print (int, optional): If set to 1, prints the output of the command. Defaults to 0.
    """
    if _print == 1:
        print("Powering off the UPS...")
        print(ups_manager.power_off_load())
    else:
        ups_manager.power_off_load()

def rebootLoad(_print=0):
    """
    Reboots the UPS after a delay (offdelay) and restarts it again.

    Args:
        _print (int, optional): If set to 1, prints the output of the command. Defaults to 0.
    """
    if _print == 1:
        print("Rebooting UPS after [delayoff] sec and restarting again, please wait...")
        print(ups_manager.reboot_load())
    else:
        ups_manager.reboot_load()

def rebootStop(_print=0):
    """
    Stops an ongoing reboot or shutdown process if it's within the offdelay time.

    Args:
        _print (int, optional): If set to 1, prints the output of the command. Defaults to 0.
    """
    if _print == 1:
        print("Halting the UPS reboot...")
        print(ups_manager.stop_reboot())
    else:
        ups_manager.stop_reboot()

def batteryTest(_print=0):
    """
    Performs a quick battery test on the UPS.

    Args:
        _print (int, optional): If set to 1, prints the output of the command. Defaults to 0.
    """
    if _print == 1:
        print("Testing the UPS battery...")
        print(ups_manager.battery_test())
    else:
        ups_manager.battery_test()

def toggleBeeper(_print=0):
    """
    Toggles the beeper on the UPS.

    Args:
        _print (int, optional): If set to 1, prints the output of the command. Defaults to 0.
    """
    if _print == 1:
        print("Toggling the UPS beeper...")
        print(ups_manager.toggle_beeper())
    else:
        ups_manager.toggle_beeper()

# Example usage of the functions
if __name__ == "__main__":
    """
    Example usage of the UPSManager methods.
    """
    restartUPSServices(1)
    time.sleep(5)
    reading = readUPS()
    print(reading)
    time.sleep(2)
    rebootLoad(1)
    time.sleep(5)
    rebootStop(1)
    reading = readUPS()
    print(reading)
    time.sleep(2)
