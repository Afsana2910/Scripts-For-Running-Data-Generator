import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sys import argv, exit
from datetime import datetime, timedelta
import os, signal


class MyHandler(FileSystemEventHandler):
    

    #last_trigger = time.time()
    def killprocess(self): 

        try: 

            for line in os.popen("ps ax | grep net.iosynth.Mqtt | grep -v grep"):  
                fields = line.split() 

                pid = fields[0]  
 
                os.kill(int(pid), signal.SIGKILL)  
            print("Processes Successfully terminated") 
              
        except: 
            print("Error Encountered while running script")  
            
    def code(self):
        self.killprocess()
        #print("file was modified")
        #Include the code to run iosynth
        command = "java -cp ~/iosynth/target/iosynth-0.0.7.jar net.iosynth.Mqtt -c ~/iosynth/target/config-mqtt.json -d ~/iosynth/target/devices.json"
        os.system(command)
    def on_modified(self, event):
        if event.src_path.endswith("file.json"):
            now = datetime.now().time()
            #print(now)
            print(f'event type: {event}  path : {event.src_path}')
            self.code()
            #print("\n")




if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='~files', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
