"""
Description: This script provides the class for controlling a UPS USB device using NUT on a Linux system.

Author: Adrian Rabadan Ortiz

Date Created: May 29, 2024

Date Modified: Month DD, Year

Version: 1.0

Dependencies: 
    NUT (using driver blazer_usb for Cypress Semiconductor 0665:5161)
    ups.conf (offdelay)
    """

import subprocess

class UPSManager:
    """
    Class to manage a UPS device using command-line utilities.

    Attributes:
        ups_name (str): Name of the UPS device.
        user (str): Username for accessing UPS commands.
        password (str): Password for accessing UPS commands.
    """
    
    def __init__(self, ups_name, user, password):
        """
        Initializes the UPSManager class with the given UPS name, username, password, 
        shutdown delay, and restart delay.

        Args:
            ups_name (str): Name of the UPS device.
            user (str): Username for accessing UPS commands.
            password (str): Password for accessing UPS commands.
        """
        self.ups_name = ups_name
        self.user = user
        self.password = password


    def restart_nut_services(self):
        """
        Restarts the NUT services (nut-server and nut-monitor).

        Returns:
            str: Success message if services restarted successfully, or an error message otherwise.
        """
        try:
            subprocess.run(["sudo", "systemctl", "restart", "nut-server"], check=True)
            subprocess.run(["sudo", "systemctl", "restart", "nut-monitor"], check=True)
            return "NUT services restarted successfully."
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e.stderr.decode('utf-8')}"
    
    def _run_command(self, command):
        """
        Runs a shell command and returns the output.

        Args:
            command (str): The command to run.

        Returns:
            str: The standard output of the command, or an error message if the command fails.
        """
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"An error occurred: {e.stderr.decode('utf-8')}"
    
    def list_commands(self):
        """
        Lists available commands for the UPS device.

        Returns:
            str: The list of available commands.
        """
        command = f"upscmd -l {self.ups_name}"
        return self._run_command(command)

    def reboot_load(self):
        """
        Reboots the UPS device after a defined delay (offdelay) and restarting again.

        Returns:
            str: The output of the reboot command.
        """
        command = f"sudo upscmd -u {self.user} -p {self.password} {self.ups_name} shutdown.return"
        return self._run_command(command)
    
    def stop_reboot(self):
        """
        Stops an ongoing reboot or shutdown process if it's within the offdelay time.

        Returns:
            str: The output of the stop reboot command.
        """
        command = f"sudo upscmd -u {self.user} -p {self.password} {self.ups_name} shutdown.stop"
        return self._run_command(command)
    
    def shutdown_delay(self):
        """
        Shuts down the UPS device after a defined delay (offdelay).

        Returns:
            str: The output of the shutdown command.
        """
        command = "sudo upsdrvctl shutdown"
        return self._run_command(command)        

    def shutdown_stayoff(self):
        """
        Shuts down the UPS device after a defined delay (shutdown_delay) and restarts it after another delay (restart_delay).
        
        Returns:
            str: The output of the shutdown stay off command.
        """
        command = f"sudo upscmd -u {self.user} -p {self.password} {self.ups_name} shutdown.stayoff"
        return self._run_command(command)

    def power_off_load(self):
        """
        Immediately turns off the load on the UPS.

        Returns:
            str: The output of the power off load command.
        """
        command = f"sudo upscmd -u {self.user} -p {self.password} {self.ups_name} load.off"
        return self._run_command(command)

    def power_on_load(self):
        """
        Immediately turns on the load on the UPS.

        Returns:
            str: The output of the power on load command.
        """
        command = f"sudo upscmd -u {self.user} -p {self.password} {self.ups_name} load.on"
        return self._run_command(command)

    def get_status(self):
        """
        Retrieves the status of the UPS device.

        Returns:
            str: The status of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost"
        return self._run_command(command)

    def get_input_voltage(self):
        """
        Retrieves the input voltage of the UPS device.

        Returns:
            str: The input voltage of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost input.voltage"
        return self._run_command(command)
    
    def get_output_voltage(self):
        """
        Retrieves the output voltage of the UPS device.

        Returns:
            str: The output voltage of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost output.voltage"
        return self._run_command(command)

    def get_frequency(self):
        """
        Retrieves the input frequency of the UPS device.

        Returns:
            str: The input frequency of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost input.frequency"
        return self._run_command(command)

    def get_battery_level(self):
        """
        Retrieves the battery charge level of the UPS device.

        Returns:
            str: The battery charge level of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost battery.charge"
        return self._run_command(command)
    
    def battery_test(self):
        """
        Performs a quick battery test on the UPS device.

        Returns:
            str: The output of the battery test command.
        """
        command = f"sudo upscmd -u {self.user} -p {self.password} {self.ups_name} test.battery.start.quick"
        return self._run_command(command)

    def get_battery_voltage(self):
        """
        Retrieves the battery voltage level of the UPS device.

        Returns:
            str: The battery voltage level of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost battery.voltage"
        return self._run_command(command)

    def get_battery_runtime(self):
        """
        Retrieves the battery runtime of the UPS device.

        Returns:
            str: The battery runtime of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost battery.runtime"
        return self._run_command(command)

    def get_ups_mode(self):
        """
        Retrieves the current mode (status) of the UPS device.

        Returns:
            str: The current mode of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost ups.status"
        return self._run_command(command)

    def toggle_beeper(self):
        """
        Toggles the beeper on the UPS device.

        Returns:
            str: The output of the beeper toggle command.
        """
        command = f"sudo upscmd -u {self.user} -p {self.password} {self.ups_name} beeper.toggle"
        return self._run_command(command)


# Example usage
if __name__ == "__main__":
    """
    Example usage of the UPSManager class.
    """
    ups_manager = UPSManager("myups", "admin", "admin_password")
    
    print("UPS Status:")
    print(ups_manager.get_status())
    
    print("Battery Level:")
    print(ups_manager.get_battery_level())
    
    print("Shutdown UPS:")
    print(ups_manager.shutdown_delay())
