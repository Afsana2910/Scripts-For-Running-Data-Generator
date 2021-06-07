import os, signal
import time
import datetime
import json

def runCommandline(device_config):
    command = "/usr/bin/java -cp /home/afsana/Fall2020/Masters-Thesis/iosynth/target/iosynth-0.0.7.jar net.iosynth.Mqtt -c /home/afsana/Fall2020/Masters-Thesis/iosynth/target/config-mqtt.json -d /home/afsana/Fall2020/Masters-Thesis/iosynth/target/"+device_config
    


def killprocess(): 
    try: 
        for line in os.popen("ps ax | grep net.iosynth.Mqtt | grep -v grep"):  
            fields = line.split() 
            pid = fields[0]  
            os.kill(int(pid), signal.SIGKILL)  
    except:
        print("Error Encountered while running script") 

        

killprocess()
currentHour = str(datetime.datetime.now().hour)
print("Current hour is ",currentHour)
with open("/home/afsana/Fall2020/Masters-Thesis/iosynth/target/configure.json", "r") as f:
    data = json.load(f)
config_file = str(data[currentHour])
runCommandline(config_file)



