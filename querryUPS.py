"""
Descripci[o]
"""

from controlUPS import UPSManager

ups_manager = UPSManager("Koblenz-7016", "admin", "admin_password")

print(ups_manager.get_status())


print(ups_manager.get_battery_level())