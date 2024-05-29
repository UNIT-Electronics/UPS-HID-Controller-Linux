"""
Description: This script provides classes for control of the UPS USB device using NUT UPS on linux system.

Author: Adrian Rabadan Ortiz

Date Created: May 29, 2024

Date Modified: Month DD, Year

Version: 1.0

Dependencies: NUT

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
        Initializes the UPSManager class with the given UPS name, username, and password.

        Args:
            ups_name (str): Name of the UPS device.
            user (str): Username for accessing UPS commands.
            password (str): Password for accessing UPS commands.
        """
        self.ups_name = ups_name
        self.user = user
        self.password = password

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

    def shutdown(self):
        """
        Shuts down the UPS device by sending the appropriate command.

        Returns:
            str: The output of the shutdown command.
        """
        command = "sudo upsdrvctl shutdown"
        return self._run_command(command)

    def reboot(self):
        """
        Reboots the UPS device by sending the appropriate command.

        Returns:
            str: The output of the reboot command.
        """
        command = f"sudo upscmd -u {self.user} -p {self.password} {self.ups_name} reboot.load"
        return self._run_command(command)

    def get_status(self):
        """
        Retrieves the status of the UPS device.

        Returns:
            str: The status of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost"
        return self._run_command(command)

    def list_commands(self):
        """
        Lists available commands for the UPS device.

        Returns:
            str: The list of available commands.
        """
        command = f"upscmd -l {self.ups_name}"
        return self._run_command(command)

    def get_voltage(self):
        """
        Retrieves the input voltage of the UPS device.

        Returns:
            str: The input voltage of the UPS device.
        """
        command = f"upsc {self.ups_name}@localhost input.voltage"
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
    print(ups_manager.shutdown())
