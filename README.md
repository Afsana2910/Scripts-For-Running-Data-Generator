# Iot-Device-Emulation
The Repository provides a solution build around a real time synthetic IoT data generator Iosynth [https://github.com/Afsana2910/iosynth] to generate sensor data in order to emulate real IoT devices.

Iosynth generates data based on the device configuration file provided to it. However, it was limited to using a single device configuration file. The solution here adapts Iosynth to use different device configuration files for different time intervals resuliting in generating real looking sensor data like that of actual IoT devices.

Device configuration files are created for every 1 hour interval from a Dataset containing IoT sensor data.
The Python Script orchestrator.py manages the selection of device configuration files for each time interval by reading the JSON file configure.json. 
The script orchestrator.py has be to be executed every time interval (1 hour) which is done by the scheduler i.e. Cron job.



# Requirements
- Java
- Maven
- Python
- Cron


# Steps to use the solution with example
The Electicity_Usage.ipnyb analyses the dataset containing daily electricity consumption (KW) at the University of Tartu Delta Centre. A particular day is divided into 24 intervals each of an hour. The distribution of the data for each interval is analyzed and determined (linearly increasing, linearly decreasing and random has been implemented for now). Also other necessary parameters like minimum and maximum range, mean, deviation and slope are also deterrmined. All these information are used as parameters in the device configuration file. The following steps are to followed to use the solution:


1. Run the Electricity_usage.ipnyb notebook file to create device configuration files. Make sure to store the device configuration files in the correct folder(Here the folder name is configurations)
2. Configure the config-mqtt.json file to specify the MQTT broker URL as shown in [https://github.com/Afsana2910/iosynth]
3. Configure the cron job using the following commands
```
crontab -e
0 * * * * python orchestrator.py
```
4. Subscribe to the mqtt topic defined in the device configuration file to view the generated IoT data

NOTE: Dataset can be provided on request
