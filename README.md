# UPS-HID-Controller-Linux
This repository provides a Python API for managing UPS devices via HID USB communication on Linux Ubuntu. Leveraging the Network UPS Tools (NUT) framework, this API allows you to control power, perform shutdowns, and check UPS status with ease.

## Métodos de `UPSManager`

| Método               | Descripción                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------------|
| `restart_nut_services` | Reinicia los servicios NUT (nut-server y nut-monitor).                                              |
| `list_commands`      | Lista los comandos disponibles para el dispositivo UPS.                                               |
| `reboot_load`        | Reinicia el UPS después de un retardo definido (offdelay) y lo vuelve a encender.                     |
| `stop_reboot`        | Detiene un proceso de reinicio o apagado en curso si está dentro del tiempo de offdelay.              |
| `shutdown_delay`     | Apaga el dispositivo UPS después de un retardo definido (offdelay).                                   |
| `shutdown_stayoff`   | Apaga el dispositivo UPS y permanece apagado.                                                         |
| `power_off_load`     | Apaga inmediatamente la carga en el UPS.                                                              |
| `power_on_load`      | Enciende inmediatamente la carga en el UPS.                                                           |
| `get_status`         | Obtiene el estado actual del UPS.                                                                     |
| `get_input_voltage`  | Obtiene el voltaje de entrada actual del UPS.                                                         |
| `get_output_voltage` | Obtiene el voltaje de salida actual del UPS.                                                          |
| `get_frequency`      | Obtiene la frecuencia de entrada actual del UPS.                                                      |
| `get_battery_level`  | Obtiene el nivel de carga actual de la batería del UPS.                                               |
| `battery_test`       | Realiza una prueba rápida de la batería del UPS.                                                      |
| `get_battery_voltage`| Obtiene el voltaje actual de la batería del UPS.                                                      |
| `get_battery_runtime`| Obtiene el tiempo de ejecución restante estimado de la batería del UPS.                               |
| `get_ups_mode`       | Obtiene el estado actual del UPS (por ejemplo, en línea, en batería, etc.).                           |
| `toggle_beeper`      | Activa o desactiva el beeper del UPS.                                                                 |


## Ejemplo de Uso
A continuación se muestra un ejemplo de cómo usar la clase UPSManager:

```python
from ups_manager import UPSManager

# Crear una instancia de UPSManager
ups = UPSManager('koblenz-7016', 'admin', 'admin_password')

# Reiniciar los servicios NUT
print(ups.restart_nut_services())

# Listar los comandos disponibles
print(ups.list_commands())

# Obtener el estado del UPS
print(ups.get_status())

# Obtener el nivel de batería
print(ups.get_battery_level())

# Realizar una prueba rápida de la batería
print(ups.battery_test())

