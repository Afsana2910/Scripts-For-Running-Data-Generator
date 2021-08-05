import os, signal
import time
import datetime
import json
def runCommandline(device_config):
    command = "/usr/bin/java -cp ~/iosynth/target/iosynth-0.0.7.jar net.iosynth.Mqtt -c ~/iosynth/target/config-mqtt.json -d ~/configurations/"+device_config
    print(os.system(command))


def process(): 
       
    try: 
          
        # iterating through each instance of the proess 
        for line in os.popen("ps ax | grep net.iosynth.Mqtt | grep -v grep"):  
            fields = line.split() 
              
            # extracting Process ID from the output 
            pid = fields[0]  
              
            # terminating process  
            os.kill(int(pid), signal.SIGKILL)  
        print("Process Successfully terminated") 
          
    except: 
        print("Error Encountered while running script")  

process()
weekno = datetime.datetime.today().weekday()
currentHour = str(datetime.datetime.now().hour)
if weekno < 5:
	with open("~/configurations/configure.json", "r") as f:
        	data = json.load(f)
	config_file = str(data[currentHour])
	runCommandline(config_file)
else:  # 5 Sat, 6 Sun
	with open("~/configurations/configure.json", "r") as f:
        	data = json.load(f)
	config_file = str(data[currentHour])
	runCommandline(config_file)






