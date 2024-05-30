"""
Description: This script provides methods for controlling a UPS USB device on a linux system.

Author: Adrian Rabadan Ortiz

Date Created: May 29, 2024

Date Modified: Month DD, Year

Version: 1.0

Dependencies: NUT

"""

from controlUPS import UPSManager
import json
import time

ups_manager = UPSManager("Koblenz-7016", "admin", "admin_password")

def readUPS():

    #Create a structured data dictionary
    output_structure = { 

        "BatL" : ups_manager.get_battery_level() + ' %',
        "Vbat" : ups_manager.get_battery_voltage() + ' V',
        "Vin"  :ups_manager.get_input_voltage() + ' V',
        "Vout"  :ups_manager.get_output_voltage() + ' V',
        "Mode" : ups_manager.get_ups_mode(),
        "Freq" : ups_manager.get_frequency() + ' Hz'
    }

    # Reemplazar \n por espacio en cada valor del diccionario
    for key in output_structure:
        if isinstance(output_structure[key], str):
            output_structure[key] = output_structure[key].replace('\n', ' ').strip()

    json_output = json.dumps(output_structure, indent=4)

    return json_output

def shutDownUPS(_print=0):
    if _print == 1:
        print("Shutdown UPS after 30 secs:")
        print(ups_manager.shutdown())
    else:
        ups_manager.shutdown()

def rebootUPS(_print=0):
    if _print == 1:
        print("Rebooting UPS...")
        print(ups_manager.reboot())
    else:
        ups_manager.reboot()
    

#print(ups_manager.get_status())

reading = readUPS()
print(reading)
time.sleep(2)
#shutDownUPS(1)
#rebootUPS(1)
print(ups_manager.list_commands())
